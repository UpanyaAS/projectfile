from .import views
from django.contrib import admin
from django.urls import path, include
app_name='shopingcart'
urlpatterns = [
    path('',views.allProduCat,name='allProduCat'),
    path('<slug:c_slug>/',views.allProduCat,name='products_by_category'),
path('<slug:c_slug>/<slug:product_slug>/',views.ProDetail,name='prodCatDetail')
]
