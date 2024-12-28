from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.http import HttpResponse
from store.models import Product


# Create your views here.
def say_hello(request):
    queryset = Product.objects.order_by('title')
    return render(request , 'hello.html', {'name': 'Dhanush'})