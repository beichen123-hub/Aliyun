from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def error(request):
    return render(request, '404.html')