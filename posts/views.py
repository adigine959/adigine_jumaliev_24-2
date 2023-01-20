from django.shortcuts import render
from posts.models import Product, Review
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


def product_detail_view(request, id):
    if request.method == 'GET':
        products = Product.objects.get(id=id)
        review = Review.objects.filter(product=products)

        context = {
            "products": products,
            "reviews": review
        }

        return render(request, "products/detail.html", context=context)
