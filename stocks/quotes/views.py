from django.shortcuts import render
#import Stock from models.py info to be used at line 27-31
# line 27 -> def add_stock(request):  -update this comment if this comment is invalid
from .models import Stock

# Create your views here.

# browser request for home.html , about, contact
def home(request):
    # getting information for the APi
    import requests
    import json

    if request.method == 'POST':
        ticker = request.POST['ticker']
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_d5d97aef30904e3582a9badd3d0478b3")

        try:
            # getting the api data, after that parse the info, else show error
            api = json.loads(api_request.content)
        except Exception as error:
            api = 'Error, try again!'
        return render(request, 'home.html', {'api': api})
    else:
        return render(request, 'home.html', {'ticker': 'Please Enter a Ticker Symbol'})


def add_stock(request):
    #pull information from db
    ticker = Stock.objects.all()
    # old return render(request, 'add_stock.html', {})
    return render(request, 'add_stock.html', {'ticker':ticker})



def about(request):
    return render(request, 'about.html', {})


def contact(request):
    return render(request, 'contact.html', {})
