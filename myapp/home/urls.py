from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('personal/', views.personal, name='personal'),
    path('map/', views.map, name='map'),
    path('map/search/', views.map_search, name='map_search'),
    path('chatbot/<str:mentor_name>/<str:work_field>/', views.chatbot, name='chatbot'),
    path('end-chat-session/', views.end_chat_session, name='end_chat_session'),
]