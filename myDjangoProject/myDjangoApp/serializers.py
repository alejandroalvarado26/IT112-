from rest_framework import serializers
from .models import Bands

class BandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bands
        fields = ["id", "name", "genre", "formation_year"]