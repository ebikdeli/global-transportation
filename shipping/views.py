from django.shortcuts import render


def shipping(request):
    """In this view customer can see shipping form and fill it to register their order"""
    return render(request, 'shipping/shipping.html')
    