from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from django.core import serializers
from .models import Property
from .serializers import PropertySerializer
from .utils import get_all_properties

@cache_page(60 * 15)
def property_list(request):
    properties = get_all_properties()
    serializer = PropertySerializer(properties, many=True)
    return JsonResponse({"data": serializer.data})