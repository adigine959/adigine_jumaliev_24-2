from django.shortcuts import render
from posts.models import Product
from django.shortcuts import HttpResponse
# Create your views here.
import datetime


def main_view(request):
    if request.method == 'GET':
        return render(request, "layouts/index.html")


def product_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        context = {
            "products": products

        }
        return render(request, "products/products.html", context=context)
