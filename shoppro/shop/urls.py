from django.contrib import admin
from django.urls import path, include
from . import views
app_name='shop'
urlpatterns = [
    path('',views.AllProdCat,name='AllProdCat'),
    path('<slug:c_slug>/', views.AllProdCat, name='Prod_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.prodetail, name='ProdCatDetail'),


]