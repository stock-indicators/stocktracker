from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.cache import cache
from .models import *
from .forms import AssetsForm

def home(request):

    q = request.GET.get('q') if request.GET.get('q') != None else ''

    
    search_stocks = Assets.objects.filter(name__icontains=q)

    stocks = Assets.objects.filter()
    contex = {'stocks': stocks, 'search_stocks': search_stocks}
    return render(request, 'base/home.html', contex)





def analyzer(request, pk):
    stocks = Assets.objects.get(id=pk)
    contex = {'stock': stocks}
    return render(request, 'base/analyzer.html', contex)


def createAsset(request):
    form = AssetsForm()
    
    if request.method == 'POST':
        form = AssetsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/analyzer_form.html', context)

def updateAsset(request, pk):
    assets = Assets.objects.get(id=pk)
    form = AssetsForm(instance=assets)
    if request.method == 'POST':
        form = AssetsForm(request.POST, instance=assets) 
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/analyzer_form.html', context)

def deleteAsset(request, pk):
    assets = Assets.objects.get(id=pk)
    if request.method == 'POST':
        assets.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj':assets})



# TO COMEBACK LATER WHEN ADDING SEARCH FUNCTION
# def search_address(request):
#     asset_name = request.GET.get('asset_name')
#     asset_list = []
#     if asset_name:
#         assets_obj = Assets.objects.filter(asset_name__icontains=asset_name)

#         for assets_obj in assets_obj:
#             asset_list.append(assets_obj.asset_name)

#     return JsonResponse({'status' :200, 'data' : asset_list})