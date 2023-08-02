from django.db import models

class Room(models.Model):
    ROOM_TYPES = (
        ('single', 'Phòng đơn'),
        ('double', 'Phòng đôi'),
        ('suite', 'Suite'),
    )

    STATUS_CHOICES = (
        ('available', 'Khả dụng'),
        ('booked', 'Đã được đặt'),
        ('in_use', 'Đang sử dụng'),
    )

    room_id = models.AutoField(primary_key=True)
    room_code = models.CharField(max_length=20, unique=True)
    type = models.CharField(max_length=20, choices=ROOM_TYPES, default='single')
    room_img = models.ImageField(upload_to='room_images/', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    number_of_beds = models.PositiveIntegerField()
    check_out_count = models.PositiveIntegerField(default=0) # lượt ở
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Phòng {self.room_code}"
