from django.urls import path,include
from .views import *

# not for prod.
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('<slug:slug>/', guide, name='guide'),
    path('', guide_list_view, name='guide_list')
]


