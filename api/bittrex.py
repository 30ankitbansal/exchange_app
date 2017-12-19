import json
import requests

header = {'User-Agent': 'Mozilla/5.0'}


def api_query():
    ret = requests.get('https://bittrex.com/api/v1.1/public/getmarketsummaries', headers=header)
    data = json.loads(ret.text)
    # print(data)
    d = {}
    for item in data['result']:
        d[item['MarketName']] = {
            'ask': item['Ask'],
            'bid': item['Bid'],
            'ask_qty': item['OpenSellOrders'],
            'bid_qty': item['OpenBuyOrders']
        }
    return d

# print(api_query())