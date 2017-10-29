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
from pizzashopapp import views

from django.contrib.auth import views as auth_views

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
]
