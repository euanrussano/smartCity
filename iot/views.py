from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import City

# Create your views here.
#-------- IOT index - show city list----------------------------
def index(request):
    city_list = City.objects.order_by('-name')
    print(city_list)
    context = {
        'city_list': city_list,
    }
    return render(request, 'iot/index.html', context)

#-------- City views----------------------------

def city_detail(request, city_id):
    city = get_object_or_404(City, pk=city_id)
    return render(request, 'iot/city_detail.html', {'city': city})

def city_devices(request, city_id):
    return HttpResponse(f"You're looking at the devices of city {city_id}")

def city_events(request, city_id):
    return HttpResponse(f"You're looking at the events of city {city_id}")

#-------- Device views----------------------------
def device_detail(request, device_id):
    return HttpResponse(f"You're looking at device {device_id}")

#-------- Event views----------------------------
def event_detail(request, event_id):
    return HttpResponse(f"You're looking at event {event_id}")

#-------- Person views----------------------------
def person_detail(request, person_id):
    return HttpResponse(f"You're looking at person {person_id}")


