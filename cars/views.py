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

def get_models(request):
    proxy = request.POST['proxy']
    carplay = request.POST['carplay']
    androidauto = request.POST['androidauto']
    car_model = models.Car()
    if (proxy and carplay and androidauto):
        car_model =  models.Car.objects.filter(smartphone_integration_android_auto='Y', smartphone_integration_proxy='Y', smartphone_integration_car_play='Y').values('oem', 'model', 'standerd', 'stand_alone', 'pack')
    elif(proxy and carplay):
        car_model =  models.Car.objects.filter(smartphone_integration_android_auto='', smartphone_integration_proxy='Y', smartphone_integration_car_play='Y').values('oem', 'model', 'standerd', 'stand_alone', 'pack')
    elif(carplay and androidauto):
        car_model =  models.Car.objects.filter(smartphone_integration_android_auto='Y', smartphone_integration_proxy='', smartphone_integration_car_play='Y').values('oem', 'model', 'standerd', 'stand_alone', 'pack')
    elif(proxy and androidauto):
        car_model =  models.Car.objects.filter(smartphone_integration_android_auto='Y', smartphone_integration_proxy='Y', smartphone_integration_car_play='').values('oem', 'model', 'standerd', 'stand_alone', 'pack')
    elif(proxy):
        car_model =  models.Car.objects.filter(smartphone_integration_android_auto='', smartphone_integration_proxy='Y', smartphone_integration_car_play='').values('oem', 'model', 'standerd', 'stand_alone', 'pack')
    elif(carplay):
        car_model =  models.Car.objects.filter(smartphone_integration_android_auto='', smartphone_integration_proxy='', smartphone_integration_car_play='Y').values('oem', 'model', 'standerd', 'stand_alone', 'pack')
    elif(androidauto):
        car_model =  models.Car.objects.all().filter(smartphone_integration_android_auto='Y', smartphone_integration_proxy='', smartphone_integration_car_play='    ').values('oem', 'model', 'standerd', 'stand_alone', 'pack')
    else:
        pass
    print(car_model)
    return JsonResponse({'car_model':list(car_model)}, safe=False)

def readme(request):
    return render(request, 'readme.html')