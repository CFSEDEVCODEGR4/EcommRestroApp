# Generated by Django 4.2 on 2023-04-04 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestroApp', '0007_delete_customer_delete_restaurant'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=10)),
                ('user_name', models.CharField(max_length=40)),
                ('user_mobile', models.CharField(max_length=120)),
                ('user_email', models.CharField(max_length=20)),
                ('user_address', models.CharField(max_length=20)),
                ('user_role', models.CharField(max_length=20)),
                ('user_password', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['user_id'],
            },
        ),
    ]
