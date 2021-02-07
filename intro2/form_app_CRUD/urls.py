from django.urls import path
from . import views

app_name = 'form_app_CRUD'

urlpatterns = [
    path('register/', views.register, name='register'),
]