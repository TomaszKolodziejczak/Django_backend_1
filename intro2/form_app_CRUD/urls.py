from django.urls import path
from . import views

app_name = 'form_app_CRUD'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('task-list/', views.task_list, name='task_list'),
    path('update/<int:task_id>/', views.update, name='update'),
]