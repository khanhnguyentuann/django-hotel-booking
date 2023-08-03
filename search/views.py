from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator
from homepage.models import Room
from booking.models import Booking

def search(request):
    rooms = Room.objects.all()
    # Nhận query parameters từ yêu cầu
    room_type = request.GET.get('roomType', '')
    check_in = request.GET.get('checkin', '')
    check_out = request.GET.get('checkout', '')

    # Tìm kiếm dựa trên loại phòng
    if room_type:
        rooms = rooms.filter(type=room_type)

    # Tìm kiếm dựa trên ngày nhận và trả phòng
    if check_in and check_out:
        bookings = Booking.objects.filter(
            Q(checkin_date__range=[check_in, check_out]) |
            Q(checkout_date__range=[check_in, check_out]) |
            Q(Q(checkin_date__lte=check_in) & Q(checkout_date__gte=check_out))
        )
        booked_room_ids = bookings.values_list('room', flat=True).distinct()
        rooms = rooms.exclude(room_id__in=booked_room_ids)

    # Phân trang
    paginator = Paginator(rooms, 8)
    page_number = request.GET.get('page') # Nhận số trang từ yêu cầu
    page_obj = paginator.get_page(page_number) # Lấy đối tượng trang
    
    return render(request, 'search/room_search.html', {'rooms': page_obj})
