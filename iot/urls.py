from django.urls import path

from . import views

urlpatterns = [
    # ex: /iot/
    path('', views.index, name='index'),
    # ex: /iot/1/
    path('<int:city_id>/', views.city_detail, name='city detail'),
    # ex: /iot/1/devices
    path('<int:city_id>/devices', views.city_devices, name='city devices'),
    # ex: /iot/1/events
    path('<int:city_id>/events', views.city_events, name='city events'),
    # ex: /iot/1/devices/1/
    path('<int:city_id>/devices/<int:device_id>', views.device_detail, name='device detail'),
    # ex: /iot/1/events/1/
    path('<int:city_id>/events/<int:event_id>', views.event_detail, name='event detail'),
]