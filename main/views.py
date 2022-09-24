from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views here.

def list_view(request, id):
    list = ToDoList.objects.get(id=id)
    if request.method == "POST":
        print(request.POST)
        if request.POST.get("save"):
            for item in list.item_set.all():
                if request.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                    item.save()
                else:
                    item.complete = False

                
        elif request.POST.get("newItem"):
            txt = request.POST.get("new")

            if len(txt) > 2:
                list.item_set.create(text=txt, complete = False)
            else:
                print("Invalid")
    context = {
        "list": list
    }
    return render(request, "main/list.html", context)


def home(request):
    context = {}
    return render(request, "main/home.html", context)


def create(request):
    
    if request.method == "POST":
        form = CreateNewList(request.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = CreateNewList()
    context = {
        "form": form
    }
    return render(request, "main/create.html", context)

