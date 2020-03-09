from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from . import models
# Create your views here.
def home(request):
    cars = models.Car.objects.values('oem').distinct()
    # cars = models.Car.objects.all()
    print(cars)
    return render(request, 'home.html', {'cars': cars})

def number_and_proportion(request):
    oem = request.POST['oem']
    head_unit_type = []
    content = {}
    # cars = models.Car.objects.all().filter(oem=oem).values()
    cars_dist = models.Car.objects.values('head_unit_type').filter(oem=oem).distinct()
    cars = models.Car.objects.all().filter(oem=oem).values()
    for car in cars:
        head_unit_type.append(car['head_unit_type'])
    for each in cars_dist:
        content[each['head_unit_type']] = head_unit_type.count(each['head_unit_type'])
    content['length'] = len(cars_dist)
    print(content)
    return JsonResponse(content)