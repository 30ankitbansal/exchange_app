import json
import requests

header = {'User-Agent': 'Mozilla/5.0'}


def api_query():
    ret = requests.get('https://api.hitbtc.com/api/1/public/ticker', headers=header)
    data = json.loads(ret.text)
    # print(data)
    d = {}
    for key in data:
        d[key] = {
            'ask': data[key]['ask'],
            'bid': data[key]['bid'],
            'ask_qty': "",
            'bid_qty': ""
        }
    return d
