from django.urls import path
from new_app import views

urlpatterns = [
    # path('', views.hello),
    path('hi/', views.helloB),
    path('bartek/', views.bartek),
    path('ewa/', views.ewa),
    path('fruits/', views.fruits),
    path('<str:name>/<int:age>/', views.display_name),
    path('2/<str:name>/', views.display_name2),
    path('new-year/', views.is_it_newyear),
]