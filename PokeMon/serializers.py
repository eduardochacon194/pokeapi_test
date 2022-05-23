from dataclasses import field
from rest_framework import serializers
from PokeMon.models import pokeapi

class pokeapiSerializers(serializers.ModelSerializer):
    class Meta:
        model = pokeapi
        fields = ['id','name_poke']