from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db.models import Sum
from rest_framework import viewsets, status, generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *
from .models import *
from insurance.permissions import *


def index(request):
    return render(request, 'insurance/home.html')


@login_required()
def overview(request):
    return render(request, 'insurance/overview.html')


# ViewSets define the view behavior.

class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.order_by('gender')
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class HomeList(generics.ListCreateAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class HomeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsOwnerOnly]


@api_view()
@login_required()
def overview_api(request):
    return Response(
        {
            'num_customers': Customer.objects.count(),
            'num_drivers': Driver.objects.count(),
            'total_homes_insured': Home.objects.count(),
            'total_vehicles_insured': Vehicle.objects.count(),
            'total_homes_value': Home.objects.aggregate(Sum('purchase_price'))['purchase_price__sum'],
        }
    )


@login_required()
def user_profile(request):
    return render(request, 'insurance/profile.html')
