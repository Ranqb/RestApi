from django.http import JsonResponse

from .models import PizzaShop, Pizza, Sushi, Kavkaz, China, Russia, News
from pizzashopapp.serializers import PizzaShopSerializer, PizzaSerializer, SushiSerializer, KavkazSerializer, ChinaSerializer, RussiaSerializer, NewsSerializer

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

def client_get_kavkazs(request, pizzashop_id):
    kavkazs = KavkazSerializer(
        Kavkaz.objects.all().filter(pizzashop_id = pizzashop_id).order_by('-id'),
        many = True,
        context = {'request':request},
    ).data
    return JsonResponse({'kavkazs':kavkazs})

def client_get_russias(request, pizzashop_id):
    russias = RussiaSerializer(
        Russia.objects.all().filter(pizzashop_id = pizzashop_id).order_by('-id'),
        many = True,
        context = {'request':request},
    ).data
    return JsonResponse({'russias':russias})

def client_get_chinas(request, pizzashop_id):
    chinas = ChinaSerializer(
        China.objects.all().filter(pizzashop_id = pizzashop_id).order_by('-id'),
        many = True,
        context = {'request':request},
    ).data
    return JsonResponse({'chinas':chinas})
