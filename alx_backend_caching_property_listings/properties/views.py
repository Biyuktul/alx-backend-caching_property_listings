from rest_framework import viewsets

from alx_backend_caching_property_listings.properties.utils import get_all_properties
from .models import Property
from .serializers import PropertySerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

@method_decorator(cache_page(60 * 15), name='list') # Cache the response of the list action for 15 minutes.
class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    def get_queryset(self):
        return get_all_properties()
    
    # list() -> get_queryset() -> Property.objects.all()