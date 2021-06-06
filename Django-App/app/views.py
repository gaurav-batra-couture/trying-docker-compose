from django.http import HttpResponse
from django.core import serializers
import json

from django.views.decorators.csrf import csrf_exempt

from app.models import Coin


def coin_detail(request):
	all_coins = serializers.serialize('json',Coin.objects.all())
	
	return HttpResponse(all_coins, content_type='application/json')


@csrf_exempt
def addCoin(request):
	data = json.loads(request.body)
	
	name = data['name']
	price = data['price']

	coin = Coin(name = name, price = price)
	coin.save()

	return HttpResponse(json.dumps("Added"), content_type='application/json')