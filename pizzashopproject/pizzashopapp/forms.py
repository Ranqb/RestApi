from django import forms
from django.contrib.auth.models import User
from pizzashopapp.models import PizzaShop,Pizza,Sushi,News,Kavkaz,Russia,China

class UserForm(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')

class UserFormForEdit(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class PizzaShopForm(forms.ModelForm):
    class Meta:
        model = PizzaShop
        fields = ('name', 'phone', 'address', 'logo')

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        exclude = ('pizzashop',)

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        exclude = ('pizzashop',)

class SushiForm(forms.ModelForm):
    class Meta:
        model = Sushi
        exclude = ('pizzashop',)

class KavkazForm(forms.ModelForm):
    class Meta:
        model = Kavkaz
        exclude = ('pizzashop',)

class RussiaForm(forms.ModelForm):
    class Meta:
        model = Russia
        exclude = ('pizzashop',)

class ChinaForm(forms.ModelForm):
    class Meta:
        model = China
        exclude = ('pizzashop',)
