from django.shortcuts import render, HttpResponse
from .models import Category, Product

# Create your views here.

def index(request):
    return HttpResponse("Hello!")

def category_by_id(request, id):
    categoryObj = Category.objects.filter(categoryId=id)
    return HttpResponse(categoryObj)

def product_by_id(request, id):
    productObj = Product.objects.filter(productId=id)
    return HttpResponse(productObj)