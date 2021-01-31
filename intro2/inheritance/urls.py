from django.urls import path
from . import views

app_name='inheritance'

urlpatterns = [
    path('1/', views.first, name='first'),
    path('2/', views.second, name='second'),
]