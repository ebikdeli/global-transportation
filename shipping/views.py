from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse, JsonResponse
from .models import Company, Shipping
from .forms import ShippingModelForm
import json


def shipping(request:HttpRequest) -> HttpResponse:
    """In this view customer can see shipping form and fill it to register their order"""
    shipping_modelform = ShippingModelForm()
    companies = Company.objects.all()
    return render(request, 'shipping/shipping.html', {'form': shipping_modelform, 'companies': companies})


def shipping_order(request: HttpRequest) -> HttpResponse:
    """Register a shipping order for the customer after the customer regsiters the shipping from shipping form"""
    if request.method == 'POST':
        form_data:dict = json.loads(request.POST.get('data', None))
        if request.user.is_authenticated:
            form_data.update({'customer': request.user})
        shipping_form = ShippingModelForm(data=form_data)
        if shipping_form.is_valid():
            shipping_data = shipping_form.cleaned_data
            shipping = Shipping.objects.create(**shipping_data)
            return JsonResponse(data={'status': 'ok', 'msg': 'New shipping created',
                                      'data':
                                          {'shipping_id': shipping.id, 'shipping_code': shipping.code, 'uuid': str(shipping.uuid)}
                                    })
        else:
            print(shipping_form.errors)
            return JsonResponse(data={'status': 'nok', 'msg': 'form data did not received successfully', 'data': None})


def shipping_view(request: HttpRequest, shipping_code: str) -> HttpResponse:
    """View all the shipping of the customer"""
    try:
        shipping = Shipping.objects.get(code=shipping_code)
        return JsonResponse(data={'msg': f'You are viewing shipping id({shipping.id}) with code "{shipping_code}"'})
    except Exception as e:
        return JsonResponse(data={'msg': f'There is no shippping with code "{shipping_code}"'})
