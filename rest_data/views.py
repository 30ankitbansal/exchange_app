from django.shortcuts import render
from rest_data import utils
# Create your views here.


def home(request):
    data = utils.get_excanges_data()
    rocktrading = data['rocktrading_data']
    bittrex = data['bittrex_data']
    bxth = data['bxth_data']
    hitbtc = data['hitbtc_data']
    kraken = data['kraken_data']
    rocktrading_pair = [key for key in rocktrading]
    bittrex_pair = [key for key in bittrex]
    hitbtc_pair = [key for key in hitbtc]
    bxth_pair = [key for key in bxth]
    kraken_pair = [key for key in kraken]
    return render(request, 'rest_data/home.html', {'rocktrading': rocktrading,
                                                   'bittrex': bittrex,
                                                   'hitbtc': hitbtc,
                                                   'hitbtc_pair': hitbtc_pair,
                                                   'bittrex_pair':bittrex_pair,
                                                   'rocktrading_pair': rocktrading_pair,
                                                   'bxth': bxth,
                                                   'bxth_pair': bxth_pair,
                                                   'kraken': kraken,
                                                   'kraken_pair': kraken_pair})
