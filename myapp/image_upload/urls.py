from django.urls import path
from . import views

urlpatterns = [
    path('image/', views.image_upload, name='image_upload'),
]