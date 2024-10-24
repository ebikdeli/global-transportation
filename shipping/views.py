from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse, JsonResponse
from .models import Company, Shipping
from .forms import ShippingModelForm


def shipping(request:HttpRequest) -> HttpResponse:
    """In this view customer can see shipping form and fill it to register their order"""
    shipping_modelform = ShippingModelForm()
    return render(request, 'shipping/shipping.html', {'form': shipping_modelform})


def shipping_order(request: HttpRequest) -> HttpResponse:
    """Register a shipping order for the customer after the customer regsiters the shipping from shipping form"""
    if request.method == 'POST':
        form = ShippingModelForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            shipping_data = form.cleaned_data
            # ! Process more data here later
            return JsonResponse(data={'status': 'ok', 'msg': 'form data received successfully', 'data': shipping_data})
        else:
            return JsonResponse(data={'status': 'nok', 'msg': f'{form.errors}', 'data': None})
