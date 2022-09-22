from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

# Create your views here.

def index(request, id):
    list = ToDoList.objects.get(id=id)
    context = {
        "list": list
    }
    return render(request, "main/list.html", context)


def home(request):
    context = {}
    return render(request, "main/home.html", context)

