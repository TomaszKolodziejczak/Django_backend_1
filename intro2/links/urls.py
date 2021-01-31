from django.urls import path
from . import views

app_name = 'links'

urlpatterns = [
    path('first/', views.first, name='first'),
    path('2/', views.second, name='second'),
    path('third/<str:x>/', views.third, name='third'),
]