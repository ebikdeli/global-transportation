from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse, JsonResponse
from .models import Company, Shipping
from .forms import ShippingModelForm
import json
import random


def shipping(request:HttpRequest) -> HttpResponse:
    """In this view customer can see shipping form and fill it to register their order"""
    shipping_modelform = ShippingModelForm()
    companies = Company.objects.all()
    return render(request, 'shipping/shipping.html', {'form': shipping_modelform, 'companies': companies})


def shipping_check(request: HttpRequest) -> HttpResponse:
    """There is form in this page that user check if there is a order using shipping.code"""
    if request.method == 'GET':
        return render(request, 'shipping/shipping_check.html')
    if request.method == 'POST':
        form_data:dict = json.loads(request.POST.get('data', None))
        shipping_code = form_data['shipping_code']
        shipping_qs = Shipping.objects.filter(code=shipping_code)
        if shipping_qs.exists():
            shipping = shipping_qs.first()
            print(shipping)
            return JsonResponse(data={'status': 'ok', 'msg': f'Shipping found with code({shipping.code})',
                                        'data':
                                            {'shipping_id': shipping.id, 'shipping_code': shipping.code, 'uuid': str(shipping.uuid)}
                                        })
        else:
            return JsonResponse(data={'status': 'nok', 'msg': f'No shipping found', 'data': None})


def shipping_order(request: HttpRequest) -> HttpResponse:
    """Register a shipping order for the customer after the customer regsiters the shipping from shipping form"""
    if request.method == 'POST':
        form_data:dict = json.loads(request.POST.get('data', None))
        if request.user.is_authenticated:
            form_data.update({'customer': request.user})
        shipping_form = ShippingModelForm(data=form_data)
        if shipping_form.is_valid():
            shipping_data = shipping_form.cleaned_data
            # ! Simulate calculating shipping cost here
            random_cost = random.randint(5, 1000000)
            # ! Simulate calculating shipping cost here
            shipping_data.update({'cost': random_cost})
            shipping = Shipping.objects.create(**shipping_data)
            return JsonResponse(data={'status': 'ok', 'msg': 'New shipping created',
                                      'data':
                                          {'shipping_id': shipping.id, 'shipping_code': shipping.code, 'uuid': str(shipping.uuid)}
                                    })
        else:
            print(shipping_form.errors)
            return JsonResponse(data={'status': 'nok', 'msg': 'form data did not received successfully', 'data': None})


def shipping_view(request: HttpRequest, shipping_code: str) -> HttpResponse:
    """View all the shipping of the customer. Shipping cost must be appear here."""
    try:
        shipping = Shipping.objects.get(code=shipping_code)
        return render(request, 'shipping/shipping_view.html', {'shipping': shipping})
    except Exception as e:
        return JsonResponse(data={'msg': f'There is no shippping with code "{shipping_code}"'})
