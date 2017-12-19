# import urllib.request as request

import requests
import json

header = {'Content-Type': 'application/json',
          'User-Agent': 'Mozilla/5.0'}


class bittrex(object):
    # base_url = 'https://bittrex.com/Api/v2.0/pub/market/'

    def price_data(self):
        price = {}

        ret = requests.get('https://bittrex.com/api/v1.1/public/getticker?market=usdt-btc')
        data = json.loads(ret.text)['result']

        price['buy'], price['sell'], price['spot'], price['currency'] = data['Bid'], data['Ask'], data['Last'], 'USD'

        return price

    # # def buy_order(self):

    # # def sell_order(self):
        

class zebpay(object):
    def price_data(self):
        price = {}
        ret = requests.get('https://www.zebapi.com/api/v1/market/ticker/btc/inr')
        data = json.loads(ret.text)

        price['buy'], price['sell'], price['spot'], price['currency'], price['volume'] = data['buy'], data['sell'], data['market'], 'INR', data['volume']

        return data

    # def buy_order(self):

    # def sell_order(self):


# class unocoin(object):
#
#     def price_data(self):
#         price = {}
#
#         ret = requests.get('https://www.unocoin.com/trade?all', headers=header)
#         data = (ret.text)
#         print(data)
#
#        # price['buy'], price['sell'], price['spot'], price['currency'] = data['buy'], data['sell'], data['avg'], 'USD'
#         # print(price['buy'])
#         return price
#
#     # def buy_order(self):
#
#     # def sell_order(self):


class poloniex(object):
    def price_data(self):
        ret = requests.get('https://poloniex.com/public?command=returnTicker', headers=header, timeout=30)

        data = json.loads(ret.text)
        print('poloniex')
        print(data)
        return data
#
#     # def buy_order(self):
#
#     # def sell_order(self):


# class AppURLopener(request.FancyURLopener):
#     version = "Mozilla/5.0"


class c_cex(object):
    def price_data(self):
        price = {}

        ret = requests.get('https://c-cex.com/t/btc-usd.json', headers={'User-Agent': 'Mozilla/5.0'})

        data = json.loads(ret.text)['ticker']           # ['ticker']
        # print(data)
        price['buy'], price['sell'], price['spot'], price['currency'] = data['buy'], data['sell'], data['lastprice'], 'INR'

        return price

    # def buy_order(self):

    # def sell_order(self):


class bitpay(object):
    def price_data(self):
        price = {}
        ret = requests.get('https://bitpay.com/api/rates/btc/inr')
        # print(type(ret))
        data = json.loads(ret.text)
        price['spot'], price['currency'] = data['rate'], 'INR'
        return data

    # def buy_order(self):

    # def sell_order(self):


class coinbase(object):
    def price_data(self):
        price = {}

        ret = requests.get('https://api.coinbase.com/v2/prices/BTC-INR/spot')
        price['spot'] = json.loads(ret.text)['data']['amount']

        ret = requests.get('https://api.coinbase.com/v2/prices/BTC-INR/buy')
        price['buy'] = json.loads(ret.text)['data']['amount']

        ret = requests.get('https://api.coinbase.com/v2/prices/BTC-INR/sell')
        price['sell'] = json.loads(ret.text)['data']['amount']

        price['currency'] = 'INR'
        return price

    # def buy_order(self):

    # def sell_order(self):


def show_data():
    cbase = coinbase()
    print(cbase.price_data())
    #
    btrex = bittrex()
    print(btrex.price_data())

    # ucoin = unocoin()
    # print(ucoin.price_data())

    cex = c_cex()
    print(cex.price_data())

    bpay = bitpay()
    print(bpay.price_data())

    poloniex =poloniex()
    print(poloniex.price_data())

    zpay = zebpay()
    print(zpay.price_data())


show_data()
