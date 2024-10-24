from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse, JsonResponse
from .models import Company, Shipping
from .forms import ShippingModelForm
import json


def shipping(request:HttpRequest) -> HttpResponse:
    """In this view customer can see shipping form and fill it to register their order"""
    shipping_modelform = ShippingModelForm()
    return render(request, 'shipping/shipping.html', {'form': shipping_modelform})


def shipping_order(request: HttpRequest) -> HttpResponse:
    """Register a shipping order for the customer after the customer regsiters the shipping from shipping form"""
    if request.method == 'POST':
        raw_data:dict = json.loads(request.POST.get('data', None))
        if request.user.is_authenticated:
            raw_data.update({'customer': request.user})
        shipping_form = ShippingModelForm(data=raw_data)
        if shipping_form.is_valid():
            shipping_data = shipping_form.cleaned_data
            return JsonResponse(data={'status': 'ok', 'msg': 'form data received successfully', 'data': shipping_data})
        # ! Process more data here later
        else:
            print(shipping_form.errors)
            return JsonResponse(data={'status': 'nok', 'msg': 'form data did not received successfully', 'data': None})


def shipping_view(request: HttpRequest) -> HttpResponse:
    """View all the shipping of the customer"""
    pass
