from django.urls import path, include
from .views import property_list
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('properties/', property_list, name='property-list'),
]