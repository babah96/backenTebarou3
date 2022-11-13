from rest_framework import serializers
from .models import*

class UrgenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Urgence
        fields ='__all__'
