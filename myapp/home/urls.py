from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('personal/', views.personal, name='personal'),
    path('map/', views.map, name='map'),
]