from api import bittrex, bxth, hitbtc, kraken, therocktrading


def get_excanges_data():
    data = {
        'bittrex_data': bittrex.api_query(),
        'bxth_data': bxth.api_query(),
        'hitbtc_data': hitbtc.api_query(),
        'rocktrading_data': therocktrading.api_query(),
        'kraken_data': kraken.get_tickers()
    }
    return data
