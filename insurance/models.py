from django.db import models
from datetime import date


class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')))
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=20)
    marital_status = models.CharField(max_length=1, blank=True, choices=(
        ('M', 'Married'),
        ('S', 'Single'),
        ('W', 'Widow/Widower')
    ))


class Policy(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    insurance_amount = models.FloatField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def home_policy_status(self):
        return 'C' if self.end_date >= date.today() else 'P'
    # class Meta:
    #    abstract = True


class Home(models.Model):
    purchase_date = models.DateField()
    purchase_price = models.FloatField()
    home_type = models.CharField(max_length=1, choices=(
        ('S', 'Single family'),
        ('M', 'Multi Family'),
        ('C', 'Condominium'),
        ('T', 'Town house')
    ))
    fire_notification = models.CharField(max_length=1, choices=(
        ('1', 'has automatic fire notification'),
        ('0', 'NO automatic fire notification')
    ))
    home_security_system = models.CharField(max_length=1, choices=(
        ('1', 'has home security system'),
        ('0', 'NO home security system')
    ))
    swimming_pool = models.CharField(max_length=1, blank=True, choices=(
        ('U', 'Underground swimming pool'),
        ('O', 'Overground swimming pool'),
        ('I', 'Indoor swimming pool'),
        ('M', 'Multiple swimming pool')
    ))
    basement = models.CharField(max_length=1, choices=(
        ('1', 'has basement'),
        ('0', 'NO basement')
    ))
    policy = models.ForeignKey(Policy, on_delete=models.SET_NULL, null=True)


class Vehicle(models.Model):
    vin = models.CharField(max_length=1, primary_key=True)
    model_year = models.IntegerField()
    vehicle_status = models.CharField(max_length=1, choices=(
        ('L', 'Leased'),
        ('F', 'Financed'),
        ('O', 'Owned')
    ))
    policy = models.ForeignKey(Policy, on_delete=models.SET_NULL, null=True)


class Driver(models.Model):
    license_number = models.CharField(max_length=17)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateTimeField()


class Invoice(models.Model):
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE)
    issue_date = models.DateTimeField()
    due_date = models.DateTimeField()
    invoice_amount = models.FloatField()
