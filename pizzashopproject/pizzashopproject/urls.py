"""pizzashopproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from pizzashopapp import views, apis

from django.contrib.auth import views as auth_views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),

    url(r'^pizzashop/sign-in/$', auth_views.login,
        {'template_name':'pizzashop/sign_in.html'},
        name='pizzashop-sign-in'),

    url(r'^pizzashop/sign-out', auth_views.logout,
        {'next_page':'/'},
        name='pizzashop-sign-out'),

    url(r'^pizzashop/$', views.pizzashop_home, name='pizzashop-home'),

    url(r'^pizzashop/sign-up', views.pizzashop_sign_up, name='pizzashop-sign-up'),

    url(r'^pizzashop/account/$', views.pizzashop_account, name='pizzashop-account'),

    url(r'^pizzashop/news/$', views.pizzashop_news, name='pizzashop-news'),
    url(r'^pizzashop/news/add/$', views.pizzashop_add_news, name ='pizzashop-add-news'),
    url(r'^pizzashop/news/edit/(?P<news_id>\d+)/$', views.pizzashop_edit_news, name ='pizzashop-edit-news'),

    url(r'^pizzashop/pizza/$', views.pizzashop_pizza, name='pizzashop-pizza'),
    url(r'^pizzashop/pizza/add/$', views.pizzashop_add_pizza, name ='pizzashop-add-pizza'),
    url(r'^pizzashop/pizza/edit/(?P<pizza_id>\d+)/$', views.pizzashop_edit_pizza, name ='pizzashop-edit-pizza'),

    url(r'^pizzashop/sushi/$', views.pizzashop_sushi, name='pizzashop-sushi'),
    url(r'^pizzashop/sushi/add/$', views.pizzashop_add_sushi, name ='pizzashop-add-sushi'),
    url(r'^pizzashop/sushi/edit/(?P<sushi_id>\d+)/$', views.pizzashop_edit_sushi, name ='pizzashop-edit-sushi'),

    url(r'^pizzashop/russia/$', views.pizzashop_russia, name='pizzashop-russia'),
    url(r'^pizzashop/russia/add/$', views.pizzashop_add_russia, name ='pizzashop-add-russia'),
    url(r'^pizzashop/russia/edit/(?P<russia_id>\d+)/$', views.pizzashop_edit_russia, name ='pizzashop-edit-russia'),

    url(r'^pizzashop/kavkaz/$', views.pizzashop_kavkaz, name='pizzashop-kavkaz'),
    url(r'^pizzashop/kavkaz/add/$', views.pizzashop_add_kavkaz, name ='pizzashop-add-kavkaz'),
    url(r'^pizzashop/kavkaz/edit/(?P<kavkaz_id>\d+)/$', views.pizzashop_edit_kavkaz, name ='pizzashop-edit-kavkaz'),

    url(r'^pizzashop/china/$', views.pizzashop_china, name='pizzashop-china'),
    url(r'^pizzashop/china/add/$', views.pizzashop_add_china, name ='pizzashop-add-china'),
    url(r'^pizzashop/china/edit/(?P<china_id>\d+)/$', views.pizzashop_edit_china, name ='pizzashop-edit-china'),

    # APIS
    url(r'^api/client/pizzashops/$', apis.client_get_pizzashops),
    url(r'^api/client/pizzas/(?P<pizzashop_id>\d+)/$', apis.client_get_pizzas),
    url(r'^api/client/sushis/(?P<pizzashop_id>\d+)/$', apis.client_get_sushis),
    url(r'^api/client/kavkazs/(?P<pizzashop_id>\d+)/$', apis.client_get_kavkazs),
    url(r'^api/client/russias/(?P<pizzashop_id>\d+)/$', apis.client_get_russias),
    url(r'^api/client/chinas/(?P<pizzashop_id>\d+)/$', apis.client_get_chinas),


    url(r'^api/client/news/(?P<pizzashop_id>\d+)/$', apis.client_get_news),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
