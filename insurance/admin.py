from django.contrib import admin

from .models import *


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gender', 'street_address', 'city', 'state')


class PolicyAdmin(admin.ModelAdmin):
    list_display = ('start_date', 'end_date', 'insurance_amount', 'customer')


class HomeAdmin(admin.ModelAdmin):
    list_display = ('purchase_date', 'purchase_price', 'home_type', 'auto_fire_notification',
                    'home_security_system', 'swimming_pool', 'basement', 'policy')


admin.site.register(Policy, PolicyAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Home, HomeAdmin)
