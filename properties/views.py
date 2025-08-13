from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.http import JsonResponse
from .utils import get_all_properties


@cache_page(60 * 15)
def property_list(request):
    properties = get_all_properties()
    data = list(properties.values())
    return JsonResponse(data, safe=False)

from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .models import Property

@cache_page(60 * 15)
def property_list(request):
    properties = list(Property.objects.values())
    return JsonResponse({"properties": properties})
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .models import Property

@cache_page(60 * 15)  # Cache for 15 minutes
def property_list(request):
    properties = list(Property.objects.values())
    return JsonResponse({"properties": properties})
