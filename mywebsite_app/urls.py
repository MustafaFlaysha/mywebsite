from django.urls import path
from mywebsite_app import views

urlpatterns = [
    path('', views.mywebsite_app, name='mywebsite_app'),
]