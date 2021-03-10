from django.urls import path,include
from .views import *

# not for prod.
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', tour_list_view, name='tours'),
    path('category/<int:pk>', tour_category_view, name='category'),
    path('tour/<slug:slug>', tour_details, name='tour_details'),
    path('tour/<slug:slug>/comment', tour_comment, name='tour_comment')
]


