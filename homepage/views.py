from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Room
from booking.models import Booking

def index(request):
    rooms = Room.objects.all()
    featured_rooms = Room.objects.order_by('-check_out_count')[:4]
    
    items_per_page = 4
    paginator = Paginator(rooms, items_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'homepage/index.html', {'rooms': page_obj, 'featured_rooms': featured_rooms})



def room_detail(request, room_id):
    room = get_object_or_404(Room, room_id=room_id)
    
    if request.user.is_authenticated:
        booking = Booking.objects.filter(user=request.user, room=room, status='pending').first()
    else:
        booking = None

    return render(request, 'homepage/room_detail.html', {'room': room, 'booking': booking})




