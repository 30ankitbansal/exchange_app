import urllib.request as request

# import requests
import json

header = {'Content-Type': 'application/json',
          'User-Agent': 'Mozilla/5.0'}


class bittrex(object):
    # base_url = 'https://bittrex.com/Api/v2.0/pub/market/'

    def price_data(self):
        price = {}

        ret = request.urlopen(request.Request('https://bittrex.com/api/v1.1/public/getticker?market=usdt-btc'))
        data = json.loads(ret.read().decode('utf-8'))['result']

        price['buy'], price['sell'], price['spot'], price['currency'] = data['Bid'], data['Ask'], data['Last'], 'USD'

        return price

    # # def buy_order(self):

    # # def sell_order(self):
        

# class zebpay(object):
#     def price_data(self):
#         ret = request.urlopen(
#             request.Request('https://bittrex.com/Api/v2.0/pub/market/GetTicks?marketName=' + ccy +
#                             '&tickInterval=day&_=' + str(timestamp)))
#         data = json.loads(ret.read().decode('utf-8'))
#         return data
#
#     # def buy_order(self):
#
#     # def sell_order(self):


class unocoin(object):

    def price_data(self):
        price = {}

        ret = request.urlopen(request.Request('https://www.unocoin.com/trade?all'))
        print(type(ret))
        # ret = requests.get('https://www.unocoin.com/trade?all', headers=header).text
        data = json.loads(ret.read().decode('utf-8'))
        print(data)

        price['buy'], price['sell'], price['spot'], price['currency'] = data['buy'], data['sell'], data['avg'], 'USD'
        print(price['buy'])
        return price

    # def buy_order(self):

    # def sell_order(self):

# class poloniex(object):
#     def price_data(self):
#         ret = request.urlopen(
#             request.Request('https://bittrex.com/Api/v2.0/pub/market/GetTicks?marketName=' + ccy +
#                             '&tickInterval=day&_=' + str(timestamp)))
#         data = json.loads(ret.read().decode('utf-8'))
#         return data
#
#     # def buy_order(self):
#
#     # def sell_order(self):


# class AppURLopener(request.FancyURLopener):
#     version = "Mozilla/5.0"


class c_cex(object):
    def price_data(self):
        price = {}

        ret = request.urlopen(request.Request('https://c-cex.com/t/btc-usd.json', headers={'User-Agent': 'Mozilla/5.0'}))

        data = json.loads(ret.read().decode('utf-8'))['ticker']           # ['ticker']
        # print(data)
        price['buy'], price['sell'], price['spot'], price['currency'] = data['buy'], data['sell'], data['lastprice'], 'USD'

        return price

    # def buy_order(self):

    # def sell_order(self):


class bitpay(object):
    def price_data(self):
        ret = request.urlopen(request.Request('https://bitpay.com/bitcoin-exchange_arbitrage-rates')).read()
        print(type(ret))
        data = json.loads(ret).decode('utf-8')
        print(data)
        return data

    # def buy_order(self):

    # def sell_order(self):


class coinbase(object):
    def price_data(self):
        price = {}

        ret = request.urlopen(request.Request('https://api.coinbase.com/v2/prices/BTC-USD/spot'))
        price['spot'] = json.loads(ret.read().decode('utf-8'))['data']['amount']

        ret = request.urlopen(request.Request('https://api.coinbase.com/v2/prices/BTC-USD/buy'))
        price['buy'] = json.loads(ret.read().decode('utf-8'))['data']['amount']

        ret = request.urlopen(request.Request('https://api.coinbase.com/v2/prices/BTC-USD/sell'))
        price['sell'] = json.loads(ret.read().decode('utf-8'))['data']['amount']

        price['currency'] = 'USD'
        return price

    # def buy_order(self):

    # def sell_order(self):




def show_data():
    cbase = coinbase()
    print(cbase.price_data())

    btrex = bittrex()
    print(btrex.price_data())

    ucoin = unocoin()
    print(ucoin.price_data())

    cex = c_cex()
    print(cex.price_data())

    bpay = bitpay()
    print(bpay.price_data())


show_data()
