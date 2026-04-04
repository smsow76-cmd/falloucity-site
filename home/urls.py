from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # La page d'accueil
    path('proprietes/', views.proprietes, name='proprietes'),
    path('detail/<int:id>/', views.detail_propriete, name='detail'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('', views.index, name='home'),
    path('detail/<int:id>/', views.detail_propriete, name='detail_propriete'),
]