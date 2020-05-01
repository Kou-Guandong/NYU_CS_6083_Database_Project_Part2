from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework import viewsets
from .serializer import *
from .models import *

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum


def index(request):
    return render(request, 'insurance/home.html')


@login_required()
def overview(request):
    return render(request, 'insurance/overview.html')


# ViewSets define the view behavior.

class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.order_by('gender')
    serializer_class = CustomerSerializer


@api_view()
@login_required()
def overview_api(request):
    return Response(
        {
            'num_customers': Customer.objects.count(),
            'num_policies': Policy.objects.count(),
            'total_homes_insured': Home.objects.count(),
            'total_vehicles_insured': Vehicle.objects.count(),
            'total_homes_value': Home.objects.aggregate(Sum('purchase_price'))['purchase_price__sum'],
        }
    )


def user_profile(request):

    return render(request, 'insurance/profile.html')
