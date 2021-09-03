from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', views.ArticleViewSet, basename='article')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    # path('article/', views.article_list, name='article_list'),
    # path('article/', views.ArticleApiView.as_view(), name='article_list'),
    path('generic/article/<int:id>/', views.GenericApiViews.as_view(), name='article_list'),
    #path('detail/<str:pk>', views.article_detail, name='article_detail'),
    path('detail/<str:id>', views.ArticleDetails.as_view(), name='article_detail'),
]
