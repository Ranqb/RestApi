from rest_framework import serializers
from pizzashopapp.models import PizzaShop, Pizza, Sushi, News, Kavkaz, Russia, China

class PizzaShopSerializer(serializers.ModelSerializer):
    logo = serializers.SerializerMethodField()

    def get_logo(self, pizzashop):
        request = self.context.get('request')
        logo_url = pizzashop.logo.url
        return request.build_absolute_uri(logo_url)
    class Meta:
        model = PizzaShop
        fields = ('id', 'name', 'phone', 'address', 'logo')

class NewsSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, news):
        request = self.context.get('request')
        image_url = news.image.url
        return request.build_absolute_uri(image_url)
    class Meta:
        model = News
        fields = ('id', 'name', 'short_description', 'image')

class PizzaSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, pizza):
        request = self.context.get('request')
        image_url = pizza.image.url
        return request.build_absolute_uri(image_url)
    class Meta:
        model = Pizza
        fields = ('id', 'name', 'short_description', 'image', 'price')

class SushiSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, sushi):
        request = self.context.get('request')
        image_url = sushi.image.url
        return request.build_absolute_uri(image_url)
    class Meta:
        model = Sushi
        fields = ('id', 'name', 'short_description', 'image', 'price')

class KavkazSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, kavkaz):
        request = self.context.get('request')
        image_url = kavkaz.image.url
        return request.build_absolute_uri(image_url)
    class Meta:
        model = Kavkaz
        fields = ('id', 'name', 'short_description', 'image', 'price')

class RussiaSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, russia):
        request = self.context.get('request')
        image_url = russia.image.url
        return request.build_absolute_uri(image_url)
    class Meta:
        model = Russia
        fields = ('id', 'name', 'short_description', 'image', 'price')

class ChinaSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, china):
        request = self.context.get('request')
        image_url = china.image.url
        return request.build_absolute_uri(image_url)
    class Meta:
        model = China
        fields = ('id', 'name', 'short_description', 'image', 'price')
