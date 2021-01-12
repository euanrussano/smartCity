from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import City
from .models import Resident, Visitor
from .models import Device, StreetSign, Status
#from .models import Camera, CameraEvent, Microphone, MicrophoneEvent, Thermometer, ThermometerEvent, CO2Meter, CO2Event, InputSensor


# Create your views here.

#-------- City views ----------------------------
class CityList(generic.ListView):
    context_object_name = 'city_list'

    def get_queryset(self):
        return City.objects.order_by('-name')

class CityDetail(generic.DetailView):
    model = City

#-------- Device views----------------------------
class DeviceList(generic.ListView):
    context_object_name = 'device_list'

    def get_queryset(self):
        return Device.objects.order_by('-latitude')

class CityDeviceList(generic.ListView):
    '''
    Shows the devices inside the city radius. Obs: As cities may overlap, devices will
    appear on different cities at the same time.
    '''
    context_object_name = 'device_list'

    def get_queryset(self):
        '''
        Filter the devices according their location and city radius.
        Args:
        Returns:
            devices: a filtered list of devices according the city location and radius.
        '''

        city = City.objects.get(pk=self.kwargs['pk'])
        devices_all = Device.objects.all()
        device_ids = []
        for device in devices_all:
            if ( (device.latitude-city.latitude)**2 + (device.longitude-city.longitude)**2 )**0.5 <= city.radius:
                device_ids.append(device.pk)

        devices = Device.objects.filter(pk__in=device_ids)
        return devices

class DeviceDetail(generic.DetailView):
    model = Device


def update_device(request, device_id):
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

'''
#-------- Event views----------------------------
def event_detail(request, event_id):
    return HttpResponse(f"You're looking at event {event_id}")
'''

#-------- Resident Views ----------------------------
class ResidentList(generic.ListView):
    context_object_name = 'resident_list'

    def get_queryset(self):
        return Resident.objects.order_by('-name')

class ResidentDetail(generic.DetailView):
    model = Resident

    def post(self):
        pass

def update_resident(request, person_id):
    
    resident = Resident.objects.get(person_id=person_id)
    
    if request.POST['phone_text'] != "" :
        new_phone = request.POST['phone_text']
        resident.phone = new_phone
        

    resident.save()

    return HttpResponseRedirect(reverse("iot:resident_detail", args=(person_id,)))


#-------- Visitor Views ----------------------------
class VisitorList(generic.ListView):
    context_object_name = 'visitor_list'

    def get_queryset(self):
        return Visitor.objects.order_by('-latitude')

class VisitorDetail(generic.DetailView):
    model = Visitor

