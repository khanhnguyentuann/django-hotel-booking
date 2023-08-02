from django.contrib import admin
from .models import Booking

def accept_check_in(modeladmin, request, queryset):
    queryset.update(status='checked_in')

accept_check_in.short_description = "Chấp nhận yêu cầu check-in đã chọn"

class BookingAdmin(admin.ModelAdmin):
    list_display = ['room', 'user', 'checkin_date', 'checkout_date', 'status']
    ordering = ['status']
    actions = [accept_check_in]

admin.site.register(Booking, BookingAdmin)
