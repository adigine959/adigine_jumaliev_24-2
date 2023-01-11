from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
import datetime

def main_view(request):
    if request.method =='GET':
        return HttpResponse('hello ')

def good_view(request):
    if request.method =='GET':
        return HttpResponse ('good bye')

def data_view(request):
    if request.method =='GET':
        return HttpResponse (datetime.datetime.now())


