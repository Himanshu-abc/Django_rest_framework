from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('article/', views.article_list, name='article_list'),
    path('detail/<str:pk>',views.article_detail, name='article_detail'),

]
