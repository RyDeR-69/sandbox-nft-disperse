import httpx
import queue

from web3 import Web3
from eth_account import Account
from concurrent.futures import ThreadPoolExecutor
from loguru import logger

from config import rpc, etherscan_api

w3 = Web3(Web3.HTTPProvider(rpc))
q = queue.Queue()


def get_abi(contract_: str):
    response = httpx.get('https://api.etherscan.io/api', params={
        'module': 'contract',
        'action': 'getabi',
        'address': contract_,
        'apikey': etherscan_api,
    })
    if response.json()['status'] != '1':
        raise Exception(f'Unknown error when getting contract abi: {response} | {response.json()}')
    return response.json()['result']


def check_balance(address: str, _id: int):
    return contract.functions.balanceOf(address, _id).call()


def collect(key: str):
    try:
        address = Account.from_key(key).address
        balance = check_balance(address, nft_id)
        nonce = w3.eth.get_transaction_count(address)
        for index in range(balance):

            if q.empty():
                return True

            to = q.get()

            tx = contract.functions.safeTransferFrom(
                address, to, nft_id, 1, b''
            ).buildTransaction({
                "from": address,
                "nonce": nonce + index,
                "gas": gas_limit,
                "gasPrice": w3.toWei(gwei, 'gwei'),
                "chainId": w3.eth.chainId
            })
            # w3.eth.estimateGas(tx)
            # exit()
            signed = w3.eth.account.sign_transaction(tx, key)
            tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
            logger.success(f"TxHash: {tx_hash.hex()}")
    except Exception as e:
        logger.exception(e)


def init_queue():
    for items in wallets:
        q.put(w3.toChecksumAddress(items))


if __name__ == '__main__':
    keys = list(filter(bool, open("private_keys.txt").read().strip().split("\n")))
    wallets = list(filter(bool, open("wallets.txt").read().strip().split("\n")))

    # init address queue
    init_queue()

    gwei = float(input("enter gwei >>> "))
    gas_limit = int(input("enter gas limit >>> "))

    contract_address = w3.toChecksumAddress(input("enter contract address >>> "))
    proxy_contract = w3.toChecksumAddress(input("enter proxy contract address >>> "))
    contract_abi = get_abi(proxy_contract)  # proxy contract
    contract = w3.eth.contract(address=contract_address, abi=contract_abi)

    nft_id = int(input("enter nft id >>> "))

    with ThreadPoolExecutor(max_workers=int(input("threads >>> "))) as executor:
        executor.map(collect, keys)

