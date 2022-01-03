from django.db.models.base import Model
from django.db.models.fields import Field
from rest_framework import serializers
from .models import Vetclinics
from rest_framework.validators import UniqueTogetherValidator

class VetclinicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vetclinics
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset= Vetclinics.objects.all(),
                fields=['name']
            )
        ]
        