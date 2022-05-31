from django.shortcuts import render
from django.http import JsonResponse
from django.core.cache import cache
from .models import *



def home(request):
    return render(request, 'base/home.html')

def analyzer(request):
    return render(request, 'base/analyzer.html')

def search_address(request):
    asset_name = request.GET.get('asset_name')
    asset_list = []
    if asset_name:
        assets_obj = Assets.objects.filter(asset_name__icontains=asset_name)

        for assets_obj in assets_obj:
            asset_list.append(assets_obj.asset_name)

    return JsonResponse({'status' :200, 'data' : asset_list})