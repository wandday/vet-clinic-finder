# Generated by Django 3.2.4 on 2021-12-21 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('find_vet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vetclinics',
            name='phone_number',
            field=models.IntegerField(),
        ),
    ]