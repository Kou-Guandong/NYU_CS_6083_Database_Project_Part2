from insurance.models import *
from rest_framework import serializers

class DriverSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Driver
        fields = ['first_name', 'last_name', 'birth_date']

        