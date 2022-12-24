from django.contrib import admin
from django.urls import path
from mainApp import views
from django.contrib.auth.decorators import login_required
from mainApp.views import search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('search/', search, name='search'),
    path('asignarbloque/', views.bloque),
]
