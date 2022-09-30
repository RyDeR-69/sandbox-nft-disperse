# sandbox-nft-disperse

**<h3>Instalation</h3>**
`pip install -r requirements.txt`

**<h3>Config</h3>**

- rpc - your eth rpc (possible from [infura](https://infura.io/dashboard )).<br>
- etherscan_api - api of etherscan, register on the site, then go [here](https://etherscan.io/myapikey ) and create api
  key.<br>

**<h3>Data files</h3>**

- private_keys.txt - private keys of wallets where are nft.<br>
- wallets.txt - addresses to which nft should be transferred.<br>

**<h3>When launch</h3>**

- gwei, gas_limit - and so everything is clear, the gas limit can be viewed by other transaction, usually 100k will be
  enough.
- contract address - nft contract address.
- proxy contract - proxy contract address [img](https://imgur.com/a/lHSEHbi ).
- nft id - take from opensea from nft which you need [img](https://imgur.com/a/VIqopGc ).

**the essence of the contracts are the same, changing the nft id changes the nft that needs to be sent.**

**<h3>Caution</h3>**

- **preferably balance of all private keys <= number of wallets.**

<hr>

**<h3>Установка</h3>**
`pip install -r requirements.txt`

**<h3>Config</h3>**

- rpc - своя rpc (можно от [инфура](https://infura.io/dashboard)).<br>
- etherscan_api - апи езерскана, регаешься на сайте потом [тут](https://etherscan.io/myapikey) делаешь апи
  ключ.<br>

**<h3>Файлы</h3>**

- private_keys.txt - приват ключи акков где лежат nft.<br>
- wallets.txt - адреса на которые должны переводится nft.<br>

**<h3>Запуск</h3>**

- gwei, gas_limit - и так все понятно, газ лимит можно по транзам смотреть скок обычно надо, 100к думаю будет норм.
- contract address - аддресс контракта nft.
- proxy contract - аддресс прокси контракта [img](https://imgur.com/a/lHSEHbi).
- nft id - берешь с opensea у nft которая тебе надо [img](https://imgur.com/a/VIqopGc).

**по суть контракты те же, меняя nft id меняется nft которую надо отправить.**

**<h3>Caution</h3>**

- **желательно что бы заранее как то чекал что бы баланс всех приватников <= количество кошельков.**
