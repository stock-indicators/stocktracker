from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    # path('search/', views.search_address, name="search"),
    path('analyzer/<str:pk>/', views.analyzer, name="analyzer")
]
