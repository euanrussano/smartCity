from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Account, City
from .models import Role, Person, Resident, Visitor
from .models import Device, StreetSign, StreetLight, InformationKiosk, Status
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
    context = {
            'city':get_object_or_404(City, accountHolder_id=city_id),
            'device_lists':{
                'Street Sign': StreetSign.objects.filter(city_holder=City.objects.get(pk=city_id)),
                'Street Light': StreetLight.objects.filter(city_holder=City.objects.get(pk=city_id)),
                'Information Kiosk': InformationKiosk.objects.filter(city_holder=City.objects.get(pk=city_id))
                }
            }

    return render(request, 'iot/city_detail.html', context)

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
    

    context = {'device_name':device.get_name(), 'device': device, 'status':Status}

    return render(request, 'iot/device_detail.html', context)

def update_device(request, city_id, device_id):
    device = get_object_or_404(Device, pk=device_id)
    #print("-"*20)
    #print("request.POST['enable_disable']", request.POST['enable_disable'])
    
    if 'status' in request.POST:
        
        if request.POST['status'] == 'working':
            device.status = Status.WORKING
        elif request.POST['status'] == 'not working':
            device.status = Status.NOT_WORKING
        elif request.POST['status'] == 'maintenance':
            device.status = Status.UNDER_MAINTENANCE

    if 'enable_disable' in request.POST:
        
        if request.POST['enable_disable'] == 'enable':
            device.enabled = True
        elif request.POST['enable_disable'] == 'disable':
            device.enabled = False

    if 'streetsign_text' in request.POST:
        if request.POST['streetsign_text'] != "":
            streetsign = StreetSign.objects.get(pk=device.pk) #this will empty the parent field
            new_text = request.POST['streetsign_text']
            streetsign.text = new_text
            streetsign.__dict__.update(device.__dict__)
            device = streetsign

    device.save()

    return HttpResponseRedirect(reverse('iot:device_detail', args=(city_id, device_id)))


#-------- Event views----------------------------
def event_detail(request, event_id):
    return HttpResponse(f"You're looking at event {event_id}")

#-------- Person views----------------------------
def resident_list(request):
    
    resident_list = Resident.objects.order_by('-name')
    
    context = {
        'resident_list': resident_list,
    }
    return render(request, 'iot/resident_list.html', context)


def resident_detail(request, person_id):
    
    
    resident = Resident.objects.get(person_id=person_id)
    
    context = {
            'resident': resident,
            }

    return render(request, 'iot/resident_detail.html', context)

def update_resident(request, person_id):
    
    resident = Resident.objects.get(person_id=person_id)
    
    if request.POST['phone_text'] != "" :
        new_phone = request.POST['phone_text']
        resident.phone = new_phone
        

    resident.save()

    return HttpResponseRedirect(reverse("iot:resident_detail", args=(person_id,)))