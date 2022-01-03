from re import search
import re
from django.shortcuts import render, redirect
from django.template import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import filters, generics
import requests
from django.contrib import messages


from .serializers import VetclinicsSerializer
from .models import Vetclinics

# Create your views here.

def index(request):
    return render(request, 'index.html')

def find(request):
    if request.method == 'POST':
        city = request.POST['city']
        if city.strip() == "":
            messages.info(request, 'Please, enter a valid city or state' )
            return render(request, 'find.html')
        response = requests.get(f'http://127.0.0.1:8000/?search={city}').json()
        if response:
            return render(request, 'find.html', {'response':response})
        else:
            messages.info(request, 'Sorry, we could not locate a vet clinic in ' + city )
            return render(request, 'find.html')

    

class FindView(generics.ListCreateAPIView):
    # def get(self, request, *args, **kwargs):
    queryset = Vetclinics.objects.all()
    serializer_class = VetclinicsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['city', 'state']
    #     return Response(serializer.data)
        

    # def post(self, request, *args, **kwargs):
    #     serializer = VetclinicsSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors)
    



