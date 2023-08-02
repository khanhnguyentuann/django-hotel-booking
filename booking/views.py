from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Room, Booking
from django.contrib import messages

@login_required
def booking(request):
    # Lấy tất cả các đơn đặt phòng của người dùng hiện tại
    bookings = Booking.objects.filter(user=request.user).exclude(status='checked_out')
    checked_out_bookings = Booking.objects.filter(user=request.user, status='checked_out')

    return render(request, 'booking/booking.html', {'bookings': bookings, 'checked_out_bookings': checked_out_bookings})
 


@login_required
def book_room(request):
    if request.method == 'POST':
        room_id = request.POST.get('room_id')
        checkin_date = request.POST.get('checkin')
        checkout_date = request.POST.get('checkout')
        user = request.user

        room = get_object_or_404(Room, pk=room_id)
        
        # Kiểm tra xem người dùng đã có đặt phòng nào với phòng này chưa
        existing_booking = Booking.objects.filter(room=room, user=user, status='pending').exists()
        if existing_booking:
            messages.error(request, 'Bạn đã có một đặt phòng đang chờ thanh toán với phòng này!')
            return redirect('homepage:room_detail', room_id=room.pk)
        
        booking = Booking(room=room, user=user, checkin_date=checkin_date, checkout_date=checkout_date)
        booking.save()

        messages.success(request, 'Đặt phòng thành công! Vui lòng đến mục quản lý đặt phòng để xem trạng thái đơn đặt phòng')
        return redirect('homepage:room_detail', room_id=room.pk)
    else:
        return redirect('homepage:index')
    

def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    room = get_object_or_404(Room, pk=booking.room_id)
    booking.delete()
    room.status = 'available'
    room.save()    
    return redirect('booking:booking')


def pay_for_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    room = get_object_or_404(Room, pk=booking.room_id)
    booking.status = 'paid'
    booking.save()
    room.status = 'booked'
    room.save()
    return redirect('booking:booking')


def check_in(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    booking.status = 'checking_in'
    booking.save()
    return redirect('booking:booking')

def check_out(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    room = booking.room
    booking.status = 'checked_out'
    booking.save()
    room.check_out_count += 1  # Cập nhật số lần đã được ở
    room.save()
    return redirect('booking:booking')


