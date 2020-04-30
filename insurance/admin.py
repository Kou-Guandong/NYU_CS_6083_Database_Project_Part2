from django.contrib import admin

from .models import *


class InsuranceAdmin(admin.ModelAdmin):
    list_per_page = 10


class GeneralInline(admin.StackedInline):
    extra = 0
    show_change_link = True


class PolicyInline(GeneralInline):
    model = Policy


class HomeInline(GeneralInline):
    model = Home


class VehicleInline(GeneralInline):
    model = Vehicle


class DriverInline(GeneralInline):
    model = Driver


class InvoiceInline(GeneralInline):
    model = Invoice


class PaymentInline(GeneralInline):
    model = Payment


class CustomerAdmin(InsuranceAdmin):
    list_display = ('first_name', 'last_name', 'gender', 'street_address', 'city', 'state', 'active_policies')
    inlines = [PolicyInline]
    list_filter = ['gender', 'state']
    search_fields = ['first_name', 'last_name', 'street_address', 'city', 'state']


class PolicyAdmin(InsuranceAdmin):
    list_display = ('start_date', 'end_date', 'insurance_amount', 'customer', 'policy_status')
    inlines = [HomeInline, VehicleInline, InvoiceInline]
    list_filter = ['start_date', 'end_date']
    search_fields = ['start_date', 'end_date']


class HomeAdmin(InsuranceAdmin):
    list_display = ('purchase_date', 'purchase_price', 'home_type', 'auto_fire_notification',
                    'home_security_system', 'swimming_pool', 'basement', 'policy')
    list_filter = ['purchase_date', 'home_type', 'auto_fire_notification',
                   'home_security_system', 'swimming_pool', 'basement']
    search_fields = ['purchase_date']


class VehicleAdmin(InsuranceAdmin):
    list_display = ('vin', 'model_year', 'vehicle_status', 'policy')
    inlines = [DriverInline]
    list_filter = ['vehicle_status']
    search_fields = ['vin', 'model_year', 'vehicle_status', 'policy']


class DriverAdmin(InsuranceAdmin):
    list_display = ('first_name', 'last_name', 'license_number', 'birth_date', 'age')
    search_fields = ['license_number', 'first_name', 'last_name', 'birth_date']


class InvoiceAdmin(InsuranceAdmin):
    list_display = ('issue_date', 'due_date', 'policy', 'invoice_amount', 'paid', 'to_be_paid')
    search_fields = ['issue_date', 'due_date', 'invoice_amount', 'policy']
    inlines = [PaymentInline]


class PaymentAdmin(InsuranceAdmin):
    list_display = ('payment_date', 'payment_amount', 'invoice')
    search_fields = ['payment_date', 'payment_amount', 'invoice']


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Policy, PolicyAdmin)
admin.site.register(Home, HomeAdmin)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Driver, DriverAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Payment, PaymentAdmin)
