from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_list, name='user_list'),
    path('addresses/', views.address_list, name='address_list'),
]
