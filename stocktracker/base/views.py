from django.shortcuts import render



def home(request):
    return render(request, 'base/home.html')

def analyzer(request):
    return render(request, 'base/analyzer.html')