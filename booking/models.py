from django.db import models
from django.contrib.auth.models import User
from homepage.models import Room

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    checkin_date = models.DateField()
    checkout_date = models.DateField()

    STATUS_CHOICES = [
        ('pending', 'Đang chờ thanh toán'),
        ('paid', 'Đã thanh toán'),
        ('checking_in', 'Đang check in'),
        ('checked_in', 'Đang sử dụng'),
        ('checked_out', 'Đã check out'),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
    )

    def get_estimated_cost(self):
        num_days = (self.checkout_date - self.checkin_date).days
        return num_days * self.room.price

    def save(self, *args, **kwargs):
        if self.status == 'pending':
            self.room.status = 'available'
        elif self.status == 'paid':
            self.room.status = 'booked'
        elif self.status == 'checking_in':
            self.room.status = 'booked'
        elif self.status == 'checked_in':
            self.room.status = 'in_use'
        elif self.status == 'checked_out':
            self.room.status = 'available'
        else:
            pass

        self.room.save()
        super().save(*args, **kwargs)
