from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    path('', views.booking, name='booking'),
    path('book_room/', views.book_room, name='book_room'),
    path('cancel-booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('pay-for-booking/<int:booking_id>/', views.pay_for_booking, name='pay_for_booking'),
    path('check_in/<int:booking_id>/', views.check_in, name='check_in'),
    path('check_out/<int:booking_id>/', views.check_out, name='check_out'),
]
