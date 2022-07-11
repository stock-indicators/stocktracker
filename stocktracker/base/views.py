from django.shortcuts import render
from django.http import JsonResponse
from django.core.cache import cache
from .models import *


def home(request):
    stocks = Assets.objects.all()
    contex = {'stocks': stocks}
    return render(request, 'base/home.html', contex)





def analyzer(request, pk):
    stocks = Assets.objects.get(id=pk)
    contex = {'stock': stocks}
    return render(request, 'base/analyzer.html', contex)





# TO COMEBACK LATER WHEN ADDING SEARCH FUNCTION
# def search_address(request):
#     asset_name = request.GET.get('asset_name')
#     asset_list = []
#     if asset_name:
#         assets_obj = Assets.objects.filter(asset_name__icontains=asset_name)

#         for assets_obj in assets_obj:
#             asset_list.append(assets_obj.asset_name)

#     return JsonResponse({'status' :200, 'data' : asset_list})