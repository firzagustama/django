from django.shortcuts import render, redirect, HttpResponse
from . import models as User
from . import forms

# Create your views here.
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'status': request.GET.get('status', False)})

    username = request.POST.get('username', False)
    password = request.POST.get('password', False)

    if not User.Detail.objects.filter(username=username, password=password).exists():
        return redirect('/login?status=failed')

    user = User.Detail.objects.get(username=username, password=password)
    request.session['user_id'] = user.id
    return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('login')

def index(request):
    if not request.session.get['user_id']:
        return redirect('login')

    context = {
        'status': request.GET.get('status', False),
        'details': User.Detail.objects.all()
    }
    return render(request, 'user/index.html', context)


def edit(request, id):
    user = User.Detail.objects.get(id=id)
    data = {
        'fullname': user.fullname,
        'address': user.address
    }
    context = {
        'id': id,
        'form': forms.DetailForm(data),
    }
    return render(request, 'user/edit.html', context)


def update(request, id):
    user = User.Detail.objects.get(id=id)
    user.fullname = request.POST['fullname']
    user.address = request.POST['address']
    user.save()

    return redirect('/?status=success')


def portfolio(request):
    if not request.session.get('user_id', ''):
        return redirect('/login/')

    id = request.session['user_id']
    context = {
        'status': request.GET.get('status', False),
        'sell': request.GET.get('sell', False),
        'detail': User.Detail.objects.get(id=id),
        'portfolio': User.Portfolio.objects.filter(user_id=id)
    }
    return render(request, 'user/portfolio.html', context)


def reksadana(request):
    id = request.session.get('user_id', False)

    if request.method == 'GET':
        context = {
            'user_id': id,
            'form': forms.ReksadanaCreateForm
        }
        return render(request, 'user/reksadana.html', context)

    total_price = int(request.POST['price']) * int(request.POST['number'])

    user = User.Detail.objects.get(id=id)
    if total_price > user.cash:
        return redirect('/?status=failed')
    user.cash -= total_price
    user.save()

    data = User.Portfolio(
        user_id=user,
        name=request.POST.get('name', False),
        price=request.POST.get('price', False),
        number=request.POST.get('number', False),
    )
    data.save()

    return redirect('/?status=success')

def reksadana_sell(request, id):
    user_id = request.session.get('user_id', False)

    user = User.Detail.objects.get(id=user_id)
    por = User.Portfolio.objects.get(id=id)

    total = por.price * por.number

    user.cash += total
    user.experience += get_exp(total)
    user.level += get_lvl(user.experience)
    user.save()

    por.delete()

    return redirect('/?sell=success')

def reksadana_sell_all(request):
    user_id = request.session.get('user_id', False)
    user = User.Detail.objects.get(id=user_id)
    por = User.Portfolio.objects.filter(user_id=user_id)

    for item in por:
        total = item.price * item.number

        user.cash += total
        user.experience += get_exp(total)
        user.level += get_lvl(user.experience)

        item.delete()

    user.save()
    return redirect('/?sell=success')


def get_exp(amount):
    return amount / 1000

def get_lvl(exp):
    return exp / 1000