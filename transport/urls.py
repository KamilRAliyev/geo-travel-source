from django.urls import path,include
from .views import *

# not for prod.
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('rentacar/', car_rental_list, name='car-rental-list'),
    path('rentacar/car/<slug:slug>', vehicle_details, name='vehicle_details'),
    path('rentacar/car/<slug:slug>/order', vehicle_order, name='vehicle_order'),
    path('transfer/', transfer, name='transfer'),
    path('<slug:slug>', transfer_static_page, name='transfer_static')
]
