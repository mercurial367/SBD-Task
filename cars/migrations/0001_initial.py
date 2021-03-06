# Generated by Django 3.0.4 on 2020-03-08 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oem', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('segment', models.CharField(max_length=50)),
                ('varient', models.CharField(max_length=100)),
                ('head_units', models.CharField(max_length=100)),
                ('head_unit_type', models.CharField(max_length=75)),
                ('standerd', models.CharField(max_length=2)),
                ('stand_alone', models.CharField(max_length=2)),
                ('pack', models.CharField(max_length=2)),
                ('input_central_controller', models.CharField(max_length=2)),
                ('input_touch_screen', models.CharField(max_length=2)),
                ('input_handwriting_recog', models.CharField(max_length=2)),
                ('smartphone_integration_proxy', models.CharField(max_length=2)),
                ('smartphone_integration_car_play', models.CharField(max_length=2)),
                ('smartphone_integration_android_auto', models.CharField(max_length=2)),
            ],
        ),
    ]
