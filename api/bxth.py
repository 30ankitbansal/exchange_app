import json
import requests

header = {'User-Agent': 'Mozilla/5.0'}


def api_query():
    ret = requests.get('https://bx.in.th/api/', headers=header)
    data = json.loads(ret.text)
    d = {}
    for key in data:
        market = "-".join([data[key]['primary_currency'], data[key]['secondary_currency']])
        d[market] = {
            'ask': data[key]['orderbook']['asks']['highbid'],
            'bid': data[key]['orderbook']['bids']['highbid'],
            'ask_qty': data[key]['orderbook']['asks']['total'],
            'bid_qty': data[key]['orderbook']['bids']['total']
        }
    return d
