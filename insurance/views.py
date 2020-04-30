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
def overviewAPI(request):
    return Response(
        {
            'num_customers': Customer.objects.count(),
            'num_policies': Policy.objects.count(),
            'total_homes_insured': Home.objects.count(),
            'total_vehicles_insured': Vehicle.objects.count(),
            'total_homes_value': Home.objects.aggregate(Sum('purchase_price'))['purchase_price__sum'],
        }
    )

def verify(request):
    u = request.POST['username']
    p = request.POST['password']
    user = authenticate(username=u, password=p)
    if user is not None:
        if user.is_active:
            # You need to call `login` with `request` AND `user`
            login(request, user)
            print("logged in")
            return redirect('/')
    else:
        return redirect('/accounts/login/')



#
# @login_required(login_url='/accounts/login/')
# def my_view(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         # Redirect to a success page.
#         print('login ok')
#     else:
#         # Return an 'invalid login' error message.
#         print('not valid login')
