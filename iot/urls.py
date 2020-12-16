from django.urls import path

from . import views

app_name = 'iot'
urlpatterns = [
    # ex: /iot/
    path('', views.index, name='index'),
    # ex: /iot/1/
    path('<int:city_id>/', views.city_detail, name='city_detail'),
    
    # ex: /iot/1/events
    path('<int:city_id>/events', views.city_events, name='city_events'),
    
    # ex: /iot/1/devices/device_type/1/
    path('<int:city_id>/devices/<int:device_id>', views.device_detail, name='device_detail'),
    # ex: /iot/1/events/event_type/1/
    path('<int:city_id>/events/<int:event_id>', views.event_detail, name='event_detail'),

    # ex: /iot/1/devices/1/update_device/
    path('<int:city_id>/devices/<int:device_id>/update_device', views.update_device, name='update_device'),

    # ex: /iot/residents/
    path('residents', views.resident_list, name='resident_list'),
    # ex: /iot/person/1/
    path('residents/<int:person_id>/', views.resident_detail, name='resident_detail'),
    # ex: /iot/person/1/
    path('residents/<int:person_id>/update_person', views.update_resident, name='update_resident'),
]