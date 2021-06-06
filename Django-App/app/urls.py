from django.urls import path

from . import views



urlpatterns = [

    path('get', views.coin_detail, name="coin_detail"),
    path('add', views.addCoin, name="addCoin"),

]