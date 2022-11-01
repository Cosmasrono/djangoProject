from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from.import views

def home(request):
    return HttpResponse("home page")

urlpatterns = [
    path("", views.home, name="home"),
]
