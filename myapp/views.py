from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Category
# Create your views here.

def index(request):
    #return HttpResponse("hello")
    category = Category.objects.all()
    context = {
        "category":category
    }
    return render(request,'myapp/index.html',context)
