import json
import requests
header = {'User-Agent': 'Mozilla/5.0'}


def api_query(command, req={}):
    if command == "returnBooks":
        ret = requests.get('https://api.kraken.com/0/public/AssetPairs', headers=header)
        return json.loads(ret.text)['result'].keys()

    if command == "returnTicker":
        ret = requests.get(
            "https://api.kraken.com/0/public/Ticker?pair=" + str(req['currencyPair']), headers=header)
        try:
            return json.loads(ret.text)
        except Exception as e:
            return


def get_tickers():
    pairs = api_query('returnBooks')
    pairs_list = [str(pair.split(".")[0]) for pair in pairs]
    pairs_dump = ",".join(pairs_list)
    data = api_query('returnTicker', {'currencyPair': pairs_dump})['result']
    if data is not None:
        d = {}
        for item in data:
            d[item] = {
                'ask': data[item]['a'][0],
                'bid': data[item]['b'][0],
                'ask_qty': data[item]['a'][2],
                'bid_qty': data[item]['b'][2]
            }
        return d 



