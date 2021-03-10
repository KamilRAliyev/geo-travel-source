from django.urls import path, include
from .views import *

# not for prod.


urlpatterns = [
    path("", home_page, name='home'),
    path('contact/', contact),
    path('visa/e-visa/', e_visa, name='e_visa'),
    path('visa/e-visa/order/', e_visa_order, name='e_visa_order'),
    path('about/who-we-are/', who_we_are, name='who-we-are'),
    path('about/where-you-can-meet-us/', where_you_can_meet_us, name='where-you-can-meet-us'),
    path('about/our-mission/', our_mission, name='our-mission'),
    path('about/sahman/', sahman, name='sahman'),
    path('policies/cookie', cookie_policy, name='cookie-policy'),
    # path('error', e404) Testing 404 error locally
]


