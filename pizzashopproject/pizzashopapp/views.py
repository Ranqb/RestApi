from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from pizzashopapp.forms import UserForm, PizzaShopForm, UserFormForEdit, NewsForm, PizzaForm, SushiForm, KavkazForm,RussiaForm,ChinaForm
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login

from pizzashopapp.models import Pizza, Sushi, Kavkaz, Russia, China, News

# Create your views here.
def home(request):
    return redirect(pizzashop_home)

@login_required(login_url='/pizzashop/sign-in/')
def pizzashop_home(request):
    return redirect(pizzashop_pizza)

@login_required(login_url='/pizzashop/sign-in/')
def pizzashop_account(request):
    user_form = UserFormForEdit(instance=request.user)
    pizzashop_form = PizzaShopForm(instance=request.user.pizzashop)

    if request.method == "POST":
        user_form = UserFormForEdit(request.POST, instance=request.user)
        pizzashop_form = PizzaShopForm(request.POST, request.FILES, instance=request.user.pizzashop)

        if user_form.is_valid() and pizzashop_form.is_valid():
            user_form.save()
            pizzashop_form.save()

    return render(request, 'pizzashop/account.html', {
        'user_form':user_form,
        'pizzashop_form':pizzashop_form,
    })

def pizzashop_sign_up(request):
    user_form = UserForm()
    pizzashop_form = PizzaShopForm()

    if request.method == "POST":
        user_form = UserForm(request.POST)
        pizzashop_form = PizzaShopForm(request.POST, request.FILES)

        if user_form.is_valid() and pizzashop_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_pizzashop = pizzashop_form.save(commit=False)
            new_pizzashop.owner = new_user
            new_pizzashop.save()

            login(request, authenticate(
                username = user_form.cleaned_data['username'],
                password = user_form.cleaned_data['password']
            ))

            return redirect(pizzashop_home)

    return render(request, 'pizzashop/sign_up.html', {
        'user_form':user_form,
        'pizzashop_form':pizzashop_form,
    })

#pizza

@login_required(login_url='/pizzashop/sign-in/')
def pizzashop_pizza(request):
    pizzas = Pizza.objects.filter(pizzashop = request.user.pizzashop).order_by("-id")
    return render(request, 'pizzashop/pizza.html', {
        'pizzas':pizzas,
    })

@login_required(login_url='/pizzashop/sign-in/')
def pizzashop_add_pizza(request):
    form = PizzaForm()
    if request.method == "POST":
        form = PizzaForm(request.POST, request.FILES)
        if form.is_valid():
            pizza = form.save(commit=False)
            pizza.pizzashop = request.user.pizzashop
            pizza.save()
            return redirect(pizzashop_pizza)

    return render(request, 'pizzashop/add_pizza.html', {
        'form':form
    })

@login_required(login_url='/pizzashop/sign-in/')
def pizzashop_edit_pizza(request, pizza_id):
    form = PizzaForm(instance = Pizza.objects.get(id = pizza_id))
    if request.method == "POST":
        form = PizzaForm(request.POST, request.FILES, instance = Pizza.objects.get(id = pizza_id))
        if form.is_valid():
            pizza = form.save()
            return redirect(pizzashop_pizza)

    return render(request, 'pizzashop/edit_pizza.html', {
        'form':form
    })

#sushi
@login_required(login_url='/pizzashop/sign-in/')
def pizzashop_sushi(request):
    sushis = Sushi.objects.filter(pizzashop = request.user.pizzashop).order_by("-id")
    return render(request, 'pizzashop/sushi.html', {
        'sushis':sushis,
    })

@login_required(login_url='/pizzashop/sign-in/')
def pizzashop_add_sushi(request):
    form = SushiForm()
    if request.method == "POST":
        form = SushiForm(request.POST, request.FILES)
        if form.is_valid():
            sushi = form.save(commit=False)
            sushi.pizzashop = request.user.pizzashop
            sushi.save()
            return redirect(pizzashop_sushi)

    return render(request, 'pizzashop/add_pizza.html', {
        'form':form
    })

@login_required(login_url='/pizzashop/sign-in/')
def pizzashop_edit_sushi(request, sushi_id):
    form = SushiForm(instance = Sushi.objects.get(id = sushi_id))
    if request.method == "POST":
        form = SushiForm(request.POST, request.FILES, instance = Sushi.objects.get(id = sushi_id))
        if form.is_valid():
            sushi = form.save()
            return redirect(pizzashop_sushi)

    return render(request, 'pizzashop/edit_pizza.html', {
        'form':form
    })


#kavkaz
@login_required(login_url='/pizzashop/sign-in/')
def pizzashop_kavkaz(request):
    kavkazs = Kavkaz.objects.filter(pizzashop = request.user.pizzashop).order_by("-id")
    return render(request, 'pizzashop/kavkaz.html', {
        'kavkazs':kavkazs,
    })

@login_required(login_url='/pizzashop/sign-in/')
def pizzashop_add_kavkaz(request):
    form = KavkazForm()
    if request.method == "POST":
        form = KavkazForm(request.POST, request.FILES)
        if form.is_valid():
            kavkaz = form.save(commit=False)
            kavkaz.pizzashop = request.user.pizzashop
            kavkaz.save()
            return redirect(pizzashop_kavkaz)

    return render(request, 'pizzashop/add_pizza.html', {
        'form':form
    })

@login_required(login_url='/pizzashop/sign-in/')
def pizzashop_edit_kavkaz(request, kavkaz_id):
    form = KavkazForm(instance = Kavkaz.objects.get(id = kavkaz_id))
    if request.method == "POST":
        form = KavkazForm(request.POST, request.FILES, instance =Kavkaz.objects.get(id = kavkaz_id))
        if form.is_valid():
            kavkaz = form.save()
            return redirect(pizzashop_kavkaz)

    return render(request, 'pizzashop/edit_pizza.html', {
        'form':form
    })

#russia
@login_required(login_url='/pizzashop/sign-in/')
def pizzashop_russia(request):
    russias = Russia.objects.filter(pizzashop = request.user.pizzashop).order_by("-id")
    return render(request, 'pizzashop/russia.html', {
        'russias':russias,
    })

@login_required(login_url='/pizzashop/sign-in/')
def pizzashop_add_russia(request):
    form = RussiaForm()
    if request.method == "POST":
        form = RussiaForm(request.POST, request.FILES)
        if form.is_valid():
            russia = form.save(commit=False)
            russia.pizzashop = request.user.pizzashop
            russia.save()
            return redirect(pizzashop_russia)

    return render(request, 'pizzashop/add_pizza.html', {
        'form':form
    })

@login_required(login_url='/pizzashop/sign-in/')
def pizzashop_edit_russia(request, russia_id):
    form = RussiaForm(instance = Russia.objects.get(id = russia_id))
    if request.method == "POST":
        form = RussiaForm(request.POST, request.FILES, instance = Russia.objects.get(id = russia_id))
        if form.is_valid():
            russia = form.save()
            return redirect(pizzashop_russia)

    return render(request, 'pizzashop/edit_pizza.html', {
        'form':form
    })

#china
@login_required(login_url='/pizzashop/sign-in/')
def pizzashop_china(request):
    chinas = China.objects.filter(pizzashop = request.user.pizzashop).order_by("-id")
    return render(request, 'pizzashop/china.html', {
        'chinas':chinas,
    })

@login_required(login_url='/pizzashop/sign-in/')
def pizzashop_add_china(request):
    form = ChinaForm()
    if request.method == "POST":
        form = ChinaForm(request.POST, request.FILES)
        if form.is_valid():
            china = form.save(commit=False)
            china.pizzashop = request.user.pizzashop
            china.save()
            return redirect(pizzashop_china)

    return render(request, 'pizzashop/add_pizza.html', {
        'form':form
    })

@login_required(login_url='/pizzashop/sign-in/')
def pizzashop_edit_china(request, china_id):
    form = ChinaForm(instance = China.objects.get(id = china_id))
    if request.method == "POST":
        form = ChinaForm(request.POST, request.FILES, instance = China.objects.get(id = china_id))
        if form.is_valid():
            china = form.save()
            return redirect(pizzashop_china)

    return render(request, 'pizzashop/edit_pizza.html', {
        'form':form
    })


#news
@login_required(login_url='/pizzashop/sign-in/')
def pizzashop_news(request):
    newses = News.objects.filter(pizzashop = request.user.pizzashop).order_by("-id")
    return render(request, 'pizzashop/news.html', {
        'newses':newses,
    })

@login_required(login_url='/pizzashop/sign-in/')
def pizzashop_add_news(request):
    form = NewsForm()
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save(commit=False)
            news.pizzashop = request.user.pizzashop
            news.save()
            return redirect(pizzashop_news)

    return render(request, 'pizzashop/add_pizza.html', {
        'form':form
    })

@login_required(login_url='/pizzashop/sign-in/')
def pizzashop_edit_news(request, news_id):
    form = NewsForm(instance = News.objects.get(id = news_id))
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES, instance = News.objects.get(id = news_id))
        if form.is_valid():
            news = form.save()
            return redirect(pizzashop_news)

    return render(request, 'pizzashop/edit_pizza.html', {
        'form':form
    })
