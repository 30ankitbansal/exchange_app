from django.shortcuts import render
from rest_data import utils
from api.price_data import *
# Create your views here.


def home(request):
    return render(request, 'rest_data/home.html', show_data())
