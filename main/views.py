from django.shortcuts import render
from django.http import JsonResponse


def index(request):
    # return JsonResponse(data={'status': 'success'}, safe=True)
    return render(request, 'main/index.html')
