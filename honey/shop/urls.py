from django.contrib import admin
from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
    path('', views.honey, name='honey'),
    path('order', views.form_order, name='order'),
    path('contact', views.contact, name='contact'),
    path('sorts', views.sorts, name='sorts'),
    path('about_us', views.about_us, name='about_us')
]