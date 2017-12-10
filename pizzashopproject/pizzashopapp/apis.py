from django.http import JsonResponse

from .models import PizzaShop, Pizza, Sushi, News
from pizzashopapp.serializers import PizzaShopSerializer, PizzaSerializer, SushiSerializer, NewsSerializer

def client_get_pizzashops(request):
    pizzashops = PizzaShopSerializer(
        PizzaShop.objects.all().order_by('-id'),
        many = True,
        context = {'request':request},
    ).data

    return JsonResponse({'pizzashops':pizzashops})

def client_get_news(request, pizzashop_id):
    news = NewsSerializer(
        News.objects.all().filter(pizzashop_id = pizzashop_id).order_by('-id'),
        many = True,
        context = {'request':request},
    ).data
    return JsonResponse({'news':news})

def client_get_pizzas(request, pizzashop_id):
    pizzas = PizzaSerializer(
        Pizza.objects.all().filter(pizzashop_id = pizzashop_id).order_by('-id'),
        many = True,
        context = {'request':request},
    ).data
    return JsonResponse({'pizzas':pizzas})

def client_get_sushis(request, pizzashop_id):
    sushis = SushiSerializer(
        Sushi.objects.all().filter(pizzashop_id = pizzashop_id).order_by('-id'),
        many = True,
        context = {'request':request},
    ).data
    return JsonResponse({'sushis':sushis})
