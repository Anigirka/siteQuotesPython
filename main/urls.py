from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('search', views.search_result, name='search'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),

    ]