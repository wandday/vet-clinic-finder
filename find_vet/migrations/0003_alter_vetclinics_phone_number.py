# Generated by Django 3.2.4 on 2021-12-22 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('find_vet', '0002_alter_vetclinics_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vetclinics',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
    ]
