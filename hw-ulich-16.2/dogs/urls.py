from django.urls import path
from . import views

urlpatterns = [
    path('breeds/', views.breed_list, name='breed_list'),
    path('dogs/', views.dog_list, name='dog_list'),
]
