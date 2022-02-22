from django.urls import path
from youtube_search_api import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='index')
]
