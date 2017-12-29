# import urllib.request as request

import requests
import json

header = {'Content-Type': 'application/json',
          'User-Agent': 'Mozilla/5.0'}


class bittrex(object):
    # base_url = 'https://bittrex.com/Api/v2.0/pub/market/'

    def price_data(self):
        price = {}

        ret = requests.get('https://bittrex.com/Api/v2.0/pub/market/GetMarketSummary?marketName=usdt-btc')
        data = json.loads(ret.text)['result']

        price['buy'], price['sell'], price['spot'], price['currency'], price['high'], price['low'], price['volume'] = \
        data['Bid'], data['Ask'], data['Last'], 'USD', data['High'], data['Low'], data['Volume']

        return price

        # # def buy_order(self):

        # # def sell_order(self):


class zebpay(object):
    def price_data(self):
        price = {}
        ret = requests.get('https://www.zebapi.com/api/v1/market/ticker/btc/usd')
        data = json.loads(ret.text)

        price['buy'], price['sell'], price['spot'], price['currency'], price['volume'] = \
            data['buy'], data['sell'], data['market'], 'USD', data['volume']

        return price

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
        price = {}
        ret = requests.get('https://poloniex.com/public?command=returnTicker', headers=header, timeout=30)
        vol = requests.get('https://poloniex.com/public?command=return24hVolume', headers=header)

        price['volume'] = json.loads(vol.text)['USDT_BTC']['BTC']

        data = json.loads(ret.text)['USDT_BTC']

        price['buy'], price['sell'], price['spot'], price['currency'], price['volume'] = data['highestBid'], data['lowestAsk'], data['last'], 'USD', data['baseVolume']

        return price


#
#     # def buy_order(self):
#
#     # def sell_order(self):


# class AppURLopener(request.FancyURLopener):
#     version = "Mozilla/5.0"


class c_cex(object):
    def price_data(self):
        price = {}

        ret = requests.get('https://c-cex.com/t/btc-usd.json', headers=header)
        vol = requests.get('https://c-cex.com/t/volume_btc.json', headers=header)

        price['volume'] = json.loads(vol.text)['ticker']['usd']['vol']

        data = json.loads(ret.text)['ticker']  # ['ticker']
        # print(data)
        price['buy'], price['sell'], price['spot'], price['currency'], price['high'], price['low'] = data['buy'], \
                                            data['sell'], data['lastprice'], 'USD', data['high'], data['low']

        return price

        # def buy_order(self):

        # def sell_order(self):


class bitpay(object):
    def price_data(self):
        price = {}
        ret = requests.get('https://bitpay.com/api/rates/btc/usd')
        # print(type(ret))
        data = json.loads(ret.text)
        price['spot'], price['currency'] = data['rate'], 'USD'

        return price

        # def buy_order(self):

        # def sell_order(self):


class coinbase(object):
    def price_data(self):
        price = {}

        ret = requests.get('https://api.coinbase.com/v2/prices/BTC-USD/spot')
        price['spot'] = json.loads(ret.text)['data']['amount']

        ret = requests.get('https://api.coinbase.com/v2/prices/BTC-USD/buy')
        price['buy'] = json.loads(ret.text)['data']['amount']

        ret = requests.get('https://api.coinbase.com/v2/prices/BTC-USD/sell')
        price['sell'] = json.loads(ret.text)['data']['amount']

        price['currency'] = 'USD'
        return price

        # def buy_order(self):

        # def sell_order(self):


def show_data():
    dict_data = {'bittrex': bittrex().price_data(),
                 'ZebPay': zebpay().price_data(),
                 'c_cex': c_cex().price_data(),
                 'Poloniex': poloniex().price_data(),
                 'bitpay': bitpay().price_data(),
                 'coinbase': coinbase().price_data()
                 }
    return dict_data


show_data()
