# Generated by Django 4.2.8 on 2025-02-04 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapi', '0007_alter_booking_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='uid',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
