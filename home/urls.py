from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('proprietes/', views.proprietes, name='proprietes'),
    path('proprietes/<int:id>/', views.detail_propriete, name='detail_propriete'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('presentation/', views.about, name='presentation'),
]