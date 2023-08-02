from django.urls import path
from . import views

app_name = 'homepage'

urlpatterns = [
    path('', views.index, name='index'),
    path('room-detail/<int:room_id>/', views.room_detail, name='room_detail'),
]
