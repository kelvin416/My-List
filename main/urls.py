from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.list_view, name="list-view"),
    path('', views.home, name="home"),
    path('create/', views.create, name="create"),

]