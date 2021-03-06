from insurance.models import *
from rest_framework import serializers


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'gender', 'street_address', 'state', 'city']


class DriverSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Driver
        fields = ['first_name', 'last_name', 'birth_date']


class HomeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Home
        fields = ['purchase_date', 'purchase_price', 'home_type', 'auto_fire_notification',
                  'home_security_system', 'swimming_pool', 'basement']


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Customer
#         fields = ['first_name', 'last_name']
