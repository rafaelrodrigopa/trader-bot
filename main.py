from binance.client import Client
from secrets import api_secret, api_key

client = Client(api_key, api_secret)


# pegar informações da nossa conta
info = client.get_account()

for item in info:
    print(item)


# ver os saldos dos ativos que temos na conta
lista_ativos = info["balances"]

# ativos que temos algum saldo
for ativo in lista_ativos:
    if float(ativo["free"]) > 0:
        print(ativo)

# criar uma ordem de compra
from binance.enums import *
order = client.create_order(
    symbol='BTCUSDT',
    side=SIDE_BUY,
    type=ORDER_TYPE_LIMIT,
    timeInForce=TIME_IN_FORCE_GTC,
    quantity=100,
    price='0.00001')