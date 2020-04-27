from django.contrib import admin

from .models import *


class PolicyInline(admin.StackedInline):
    model = Policy
    extra = 0
    show_change_link = True


class HomeInline(admin.StackedInline):
    model = Home
    extra = 0
    show_change_link = True


class VehicleInline(admin.StackedInline):
    model = Vehicle
    extra = 0
    show_change_link = True


class DriverInline(admin.StackedInline):
    model = Driver
    extra = 0
    show_change_link = True

class InvoiceInline(admin.StackedInline):
    model = Invoice
    extra = 0
    show_change_link = True


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gender', 'street_address', 'city', 'state')
    inlines = [PolicyInline]
    list_filter = ['gender', 'state']
    search_fields = ['first_name', 'last_name', 'street_address', 'city', 'state']


class PolicyAdmin(admin.ModelAdmin):
    list_display = ('start_date', 'end_date', 'insurance_amount', 'customer', 'policy_status')
    inlines = [HomeInline, VehicleInline, InvoiceInline]
    list_filter = ['start_date', 'end_date']
    search_fields = ['start_date', 'end_date']


class HomeAdmin(admin.ModelAdmin):
    list_display = ('purchase_date', 'purchase_price', 'home_type', 'auto_fire_notification',
                    'home_security_system', 'swimming_pool', 'basement', 'policy')
    list_filter = ['purchase_date', 'home_type', 'auto_fire_notification',
                   'home_security_system', 'swimming_pool', 'basement']
    search_fields = ['purchase_date']


class VehicleAdmin(admin.ModelAdmin):
    list_display = ('vin', 'model_year', 'vehicle_status', 'policy')
    inlines = [DriverInline]
    list_filter = ['vehicle_status']
    search_fields = ['vin', 'model_year', 'vehicle_status', 'policy']


class DriverAdmin(admin.ModelAdmin):
    list_display = ('license_number', 'first_name', 'last_name', 'birth_date')
    search_fields = ['license_number', 'first_name', 'last_name', 'birth_date']


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('issue_date', 'due_date', 'invoice_amount', 'policy')
    search_fields = ['issue_date', 'due_date', 'invoice_amount', 'policy']


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Policy, PolicyAdmin)
admin.site.register(Home, HomeAdmin)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Driver, DriverAdmin)
admin.site.register(Invoice, InvoiceAdmin)
