from django.shortcuts import render

# Create your views here.

# browser request for home.html
def home(request):
    return render(request, 'home.html', {})