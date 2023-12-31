# Generated by Django 4.2.2 on 2023-08-02 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_booking_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('pending', 'Đang chờ thanh toán'), ('paid', 'Đã thanh toán'), ('checking_in', 'Đang check in'), ('checked_in', 'Đang sử dụng')], default='pending', max_length=20),
        ),
    ]
