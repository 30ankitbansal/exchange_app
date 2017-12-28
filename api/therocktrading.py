import json
import time
import requests

headers ={'Content-Type': 'application/json',
          'User-Agent': 'Mozilla/5.0'}


def api_query():
    ret = requests.get('https://api.therocktrading.com/v1/funds/tickers', headers=headers)
    data = json.loads(ret.text)['tickers']
    # print(data)
    d = {}
    for item in data:
        d[item['fund_id']] = {
            'ask': item['ask'],
            'bid': item['bid'],
            'aks_qty': "",
            'bid_qty': ""
        }
    return d

api_query()