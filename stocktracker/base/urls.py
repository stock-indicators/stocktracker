from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    # path('search/', views.search_address, name="search"),
    path('analyzer/<str:pk>/', views.analyzer, name="analyzer"),
    path('create-asset/', views.createAsset, name="create-asset"),
    path('update-asset/<str:pk>/', views.updateAsset, name="update-asset"),
    path('delete-asset/<str:pk>/', views.deleteAsset, name="delete-asset"),
]
