from django.shortcuts import render
from rest_framework import generics
from PokeMon.models import pokeapi
from PokeMon.serializers import pokeapiSerializers

class pokeview(generics.ListCreateAPIView):
    queryset = pokeapi.objects.all()
    serializer_class = pokeapiSerializers

class pokedetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = pokeapi
    serializer_class = pokeapiSerializers
