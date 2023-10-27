from django.shortcuts import render

def home(request):
    context = {}
    return render(request, 'order_manager/main.html', context)

def order(request):
    context = {}
    return render(request, 'order_manager/order.html', context)