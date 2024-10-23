from django.urls import path
from . import views


app_name = 'shipping'

urlpatterns = [
    path('order/', views.shipping_order, name='order'),
    path('', views.shipping, name='shipping'),
]
