from django.urls import path
from . import views


app_name = 'shipping'

urlpatterns = [
    path('order/', views.shipping_order, name='order'),
    path('check/', views.shipping_check, name='check'),
    path('view/<str:shipping_code>/', views.shipping_view, name='view'),
    path('', views.shipping, name='shipping'),
]
