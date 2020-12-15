from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Account, City
from .models import Role, Resident, Visitor
from .models import Device, StreetSign, StreetLight, InformationKiosk
from .models import Camera, CameraEvent, Microphone, MicrophoneEvent, Thermometer, ThermometerEvent, CO2Meter, CO2Event, InputSensor


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
    
    context = {
            'city_id':city_id,
            'device_lists':{
                'streetsign': StreetSign.objects.filter(city=City.objects.get(pk=city_id)),
                'streetlight': StreetLight.objects.filter(city=City.objects.get(pk=city_id)),
                'informationkiosk': InformationKiosk.objects.filter(city=City.objects.get(pk=city_id))
                }
            }

    print(context)
    return render(request, 'iot/city_devices.html', context)

def city_events(request, city_id):
    return HttpResponse(f"You're looking at the events of city {city_id}")

#-------- Device views----------------------------
def device_detail(request, city_id, device_id):
    
    devices_list = [StreetSign, StreetLight, InformationKiosk]
    device = get_object_or_404(Device, pk=device_id)
    for device_type in devices_list:
        try:
            device = get_object_or_404(device_type, pk=device_id)
            if device:
                break
        except:
            pass
    

    context = {'device_name':device.get_name(), 'device': device}

    return render(request, 'iot/device_detail.html', context)

def update_device(request, city_id, device_id):
    device = get_object_or_404(Device, pk=device_id)
    #print("-"*20)
    #print("request.POST['enable_disable']", request.POST['enable_disable'])
    
    if 'enable_disable' in request.POST:
        
        if request.POST['enable_disable'] == 'enable':
            device.enabled = True
        elif request.POST['enable_disable'] == 'disable':
            device.enabled = False

    if request.POST['streetsign_text']:
        streetsign = StreetSign(pk=device.pk) #this will empty the parent field
        new_text = request.POST['streetsign_text']
        streetsign.text = new_text
        streetsign.__dict__.update(device.__dict__)
        device = streetsign

    device.save()

    context = {'device_name':device.get_name(), 'device': device}

    return HttpResponseRedirect(reverse('iot:device detail', args=(city_id, device_id)))

def update_streetsign(request, city_id, device_id):
    device = get_object_or_404(StreetSign, pk=device_id)
    new_text = request.POST['streetsign_text']
    device.text = new_text
    device.save()

    context = {'device_name':device.get_name(), 'device': device}

    return HttpResponseRedirect(reverse('iot:device detail', args=(city_id, device_id)))



#-------- Event views----------------------------
def event_detail(request, event_id):
    return HttpResponse(f"You're looking at event {event_id}")

#-------- Person views----------------------------
def person_detail(request, person_id):
    return HttpResponse(f"You're looking at person {person_id}")


