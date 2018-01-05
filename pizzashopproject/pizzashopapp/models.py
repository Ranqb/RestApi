from django.db import models
from django.contrib.auth.models import User
import os

# Create your models here.
class PizzaShop(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='pizzashop')
    name = models.CharField(max_length=100, verbose_name = 'Название')
    phone = models.CharField(max_length=100, verbose_name = 'Телефон')
    address = models.CharField(max_length=100, verbose_name = 'Адрес')
    logo = models.ImageField(upload_to='pizzashop_logo/', blank = False, verbose_name = 'Логотип')

    def __str__(self):
        return self.name

def news_upload_path(instance, filename):
    return os.path.join("news_images",
      "user_%s" % instance.pizzashop.owner.username, filename)

def get_pizza_upload_path(instance, filename):
    return os.path.join("pizza_images",
      "user_%s" % instance.pizzashop.owner.username, filename)

def get_sushi_upload_path(instance, filename):
    return os.path.join("sushi_images",
      "user_%s" % instance.pizzashop.owner.username, filename)

def get_kavkaz_upload_path(instance, filename):
    return os.path.join("kavkaz_images",
      "user_%s" % instance.pizzashop.owner.username, filename)

def get_russia_upload_path(instance, filename):
    return os.path.join("russia_images",
      "user_%s" % instance.pizzashop.owner.username, filename)

def get_china_upload_path(instance, filename):
    return os.path.join("china_images",
      "user_%s" % instance.pizzashop.owner.username, filename)

class News(models.Model):
    pizzashop = models.ForeignKey(PizzaShop)
    name = models.CharField(max_length=30)
    short_description = models.CharField(max_length=10000)
    image = models.ImageField(upload_to=news_upload_path, blank=False)

    def __str__(self):
        return self.name

class Pizza(models.Model):
    pizzashop = models.ForeignKey(PizzaShop)
    name = models.CharField(max_length=30)
    short_description = models.CharField(max_length=10000)
    image = models.ImageField(upload_to=get_pizza_upload_path, blank=False)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Sushi(models.Model):
    pizzashop = models.ForeignKey(PizzaShop)
    name = models.CharField(max_length=30)
    short_description = models.CharField(max_length=10000)
    image = models.ImageField(upload_to=get_sushi_upload_path, blank=False)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Kavkaz(models.Model):
    pizzashop = models.ForeignKey(PizzaShop)
    name = models.CharField(max_length=30)
    short_description = models.CharField(max_length=10000)
    image = models.ImageField(upload_to=get_kavkaz_upload_path, blank=False)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Russia(models.Model):
    pizzashop = models.ForeignKey(PizzaShop)
    name = models.CharField(max_length=30)
    short_description = models.CharField(max_length=10000)
    image = models.ImageField(upload_to=get_russia_upload_path, blank=False)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class China(models.Model):
    pizzashop = models.ForeignKey(PizzaShop)
    name = models.CharField(max_length=30)
    short_description = models.CharField(max_length=10000)
    image = models.ImageField(upload_to=get_china_upload_path, blank=False)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name
