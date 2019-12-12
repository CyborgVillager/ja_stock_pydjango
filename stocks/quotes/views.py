from django.shortcuts import render


# Create your views here.

# browser request for home.html , about, contact
def home(request):
    return render(request, 'home.html', {})


def about(request):
    return render(request, 'about.html', {})


def contact(request):
    return render(request, 'contact.html', {})
