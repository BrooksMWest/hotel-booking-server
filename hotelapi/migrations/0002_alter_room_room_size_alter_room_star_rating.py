# Generated by Django 4.2.16 on 2025-01-24 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_size',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='room',
            name='star_rating',
            field=models.IntegerField(),
        ),
    ]
