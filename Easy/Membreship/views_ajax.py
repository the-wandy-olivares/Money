from django.http import JsonResponse
from .models import Payment, Membership 
import requests, uuid

def CreatePay(request):
      data = []
      pay = Payment
      print(request.GET.get('invoice'))
      pay.objects.create(
            membership = request.user.membership,
            name_plan =  request.GET.get('name_plan') if request.GET.get('name_plan')  else '..' ,
            price_plan = int(float(request.GET.get('price_plan', 0))),
            invoice = request.GET.get('invoice'),
            id_plan = request.GET.get('id_plan'),
            id_user = request.GET.get('id_user')
      )
      return JsonResponse(list(data), safe=False)