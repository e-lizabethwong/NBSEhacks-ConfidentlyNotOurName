from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('personal/', views.personal, name='personal'),
    path('map/', views.map, name='map'),
    path('chatbot/<str:mentor_name>/', views.chatbot, name='chatbot'),
    path('end-chat-session/', views.end_chat_session, name='end_chat_session'),
]