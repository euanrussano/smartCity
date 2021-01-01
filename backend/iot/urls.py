from django.urls import path, include

from rest_framework.routers import DefaultRouter  # add this
from . import api # add this

from . import views

router = DefaultRouter()  # add this
router.register(r'cities', api.CityViewSet)  # add this
router.register(r'devices', api.DeviceViewSet)  # add this
router.register(r'residents', api.ResidentViewSet)  # add this



app_name = 'iot'
urlpatterns = [
    path("api/", include(router.urls)),

    # ex: /iot/cities
    path('cities/', views.CityList.as_view(), name='city_list'),
    # ex: /iot/cities/1/
    path('cities/<int:pk>/', views.CityDetail.as_view(), name='city_detail'),
    # ex: /iot/cities/1/devices  ----> Devices in city
    path('cities/<int:pk>/devices/', views.CityDeviceList.as_view(), name='city_device_list'),
    
    # ex: /iot/1/event/
    #path('<int:city_id>/event/', views.city_events, name='city_events'),
    
    # ex: /iot/1/devices/device_type/1/
    path('devices/', views.DeviceList.as_view(), name='device_list'),
    # ex: /iot/1/devices/device_type/1/
    path('devices/<int:pk>/', views.DeviceDetail.as_view(), name='device_detail'),
    # ex: /iot/1/events/event_type/1/
    #path('<int:city_id>/events/<int:event_id>/', views.event_detail, name='event_detail'),

    # ex: /iot/1/devices/1/update_device/
    path('devices/<int:pk>/update_device', views.update_device, name='update_device'),

    # ex: /iot/residents/
    path('residents/', views.ResidentList.as_view(), name='resident_list'),
    # ex: /iot/person/1/
    path('residents/<int:pk>/', views.ResidentDetail.as_view(), name='resident_detail'),
    # ex: /iot/person/1/
    path('residents/<int:pk>/update/', views.update_resident, name='update_resident'),
]