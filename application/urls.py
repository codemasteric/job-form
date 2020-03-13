from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('jobs/', views.home, name='home'),
    path('form/', views.submit_form, name='submit_form'),
]