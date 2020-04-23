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
    customer_type = models.CharField(max_length=2, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Policy(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    insurance_amount = models.FloatField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def home_policy_status(self):
        return 'C' if self.end_date >= date.today() else 'P'

    # class Meta:
    #    abstract = True

    def __str__(self):
        return self.customer.first_name + ' ' + self.customer.last_name + ': ' + str(self.insurance_amount)


class Home(models.Model):
    purchase_date = models.DateField()
    purchase_price = models.FloatField()
    home_type = models.CharField(max_length=1, choices=(
        ('S', 'Single family'),
        ('M', 'Multi Family'),
        ('C', 'Condominium'),
        ('T', 'Town house')
    ))
    auto_fire_notification = models.CharField(max_length=1, choices=(
        ('1', 'YES'),
        ('0', 'NO')
    ))
    home_security_system = models.CharField(max_length=1, choices=(
        ('1', 'YES'),
        ('0', 'NO')
    ))
    swimming_pool = models.CharField(max_length=1, blank=True, choices=(
        ('U', 'Underground'),
        ('O', 'Overground'),
        ('I', 'Indoor'),
        ('M', 'Multiple')
    ))
    basement = models.CharField(max_length=1, choices=(
        ('1', 'YES'),
        ('0', 'NO')
    ))
    policy = models.ForeignKey(Policy, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.policy) + ' purchased at: ' + str(self.purchase_date)


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
