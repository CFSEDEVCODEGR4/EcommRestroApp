# Generated by Django 4.2 on 2023-04-04 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestroApp', '0004_restaurantmenu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurantmenu',
            name='item_price',
        ),
        migrations.AlterField(
            model_name='restaurantmenu',
            name='item_type',
            field=models.CharField(max_length=20),
        ),
    ]
