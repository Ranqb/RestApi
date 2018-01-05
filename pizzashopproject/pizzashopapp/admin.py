from django.contrib import admin
from pizzashopapp.models import PizzaShop, Pizza, Sushi, Kavkaz, China, Russia, News
# Register your models here.

admin.site.register(PizzaShop)
admin.site.register(News)

admin.site.register(Pizza)
admin.site.register(Sushi)
admin.site.register(Kavkaz)
admin.site.register(China)
admin.site.register(Russia)
