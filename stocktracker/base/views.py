from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.cache import cache
from .models import *
from .forms import AssetsForm

def home(request):
    stocks = Assets.objects.all()
    contex = {'stocks': stocks}
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



# TO COMEBACK LATER WHEN ADDING SEARCH FUNCTION
# def search_address(request):
#     asset_name = request.GET.get('asset_name')
#     asset_list = []
#     if asset_name:
#         assets_obj = Assets.objects.filter(asset_name__icontains=asset_name)

#         for assets_obj in assets_obj:
#             asset_list.append(assets_obj.asset_name)

#     return JsonResponse({'status' :200, 'data' : asset_list})