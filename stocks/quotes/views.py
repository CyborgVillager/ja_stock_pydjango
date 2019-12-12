from django.shortcuts import render


# Create your views here.

# browser request for home.html , about, contact
def home(request):
    # getting information for the APi
    import requests
    import json
    api_request = requests.get('https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_d5d97aef30904e3582a9badd3d0478b3')

    try:
        # getting the api data, after that parse the info, else show error
        api = json.loads(api_request.content)
    except Exception as error:
        api = 'Error, try again!'
    # pk_d5d97aef30904e3582a9badd3d0478b3
    return render(request, 'home.html', {'api': api})


def about(request):
    return render(request, 'about.html', {})


def contact(request):
    return render(request, 'contact.html', {})
