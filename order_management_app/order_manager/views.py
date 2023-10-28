from django.shortcuts import render
from .models import *


def home(request):

    orders = Order.objects.all()

    context = {
        'orders': orders,
    }
    return render(request, 'order_manager/home.html', context)

def order(request):
    context = {}
    return render(request, 'order_manager/order.html', context)