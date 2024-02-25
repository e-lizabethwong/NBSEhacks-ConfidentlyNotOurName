from django.urls import path
from . import views

urlpatterns = [
    # path('upload/', views.image_upload_view, name='image-upload'),
    path('display-image/<int:image_id>/', views.analyzer, name='analyzer'),
    path('asset/', views.asset, name='asset'),
    path('', views.main, name='main'),
]