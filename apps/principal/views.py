from django.shortcuts import render

def index(request):
    return render(request, 'base/principal.html')

def registro(request):
    return render(request, 'register.html')


