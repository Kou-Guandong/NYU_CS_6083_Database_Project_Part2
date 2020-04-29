from django.db import models
from datetime import date
from django.db.models import Subquery, OuterRef


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

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def active_policies(self):
        now = date.today()
        policies = Policy.objects.filter(customer_id=self.id, start_date__lte=now, end_date__gte=now)
        return policies.count()

    def homes(self):
        now = date.today()
        policies = Policy.objects.filter(customer_id=self.id, start_date__lte=now, end_date__gte=now)
        homes = Home.objects.filter(customer_id=self.id, start_date__lte=now, end_date__gte=now)
        return homes.count()


class Policy(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    insurance_amount = models.FloatField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def policy_status(self):
        return 'C' if self.end_date >= date.today() else 'P'

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
    vin = models.CharField(max_length=17, primary_key=True)
    model_year = models.IntegerField()
    vehicle_status = models.CharField(max_length=1, choices=(
        ('L', 'Leased'),
        ('F', 'Financed'),
        ('O', 'Owned')
    ))
    policy = models.ForeignKey(Policy, on_delete=models.SET_NULL, null=True)


class Driver(models.Model):
    license_number = models.CharField(max_length=17, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    vehicle_vin = models.ForeignKey(Vehicle, db_column='vehicle_vin', on_delete=models.SET_NULL, null=True)


class Invoice(models.Model):
    issue_date = models.DateField()
    due_date = models.DateField()
    invoice_amount = models.FloatField()
    policy = models.ForeignKey(Policy, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.policy) + ', invoice issued at %s with amount %s' % (self.issue_date, self.invoice_amount)

    def paid(self):
        payments = Payment.objects.filter(invoice_id=self.id)
        paid = payments.aggregate(models.Sum('payment_amount'))['payment_amount__sum']
        return paid or 0

    def to_be_paid(self):
        return round((self.invoice_amount - self.paid()) * 100) / 100


class Payment(models.Model):
    payment_date = models.DateField()
    payment_amount = models.FloatField()
    invoice = models.ForeignKey(Invoice, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.invoice) + 'with %s'
