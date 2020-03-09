from django.db import models

# Create your models here.

class Car(models.Model):
    oem = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    segment = models.CharField(max_length=50)
    varient = models.CharField(max_length= 100)
    head_units = models.CharField(max_length=100)
    head_unit_type = models.CharField(max_length=75)
    standerd = models.CharField(max_length=2)
    stand_alone = models.CharField(max_length=2)
    pack = models.CharField(max_length=2)
    input_central_controller = models.CharField(max_length=2)
    input_touch_screen = models.CharField(max_length=2)
    input_handwriting_recog = models.CharField(max_length=2)
    smartphone_integration_proxy = models.CharField(max_length=2)
    smartphone_integration_car_play = models.CharField(max_length=2)
    smartphone_integration_android_auto = models.CharField(max_length=2)