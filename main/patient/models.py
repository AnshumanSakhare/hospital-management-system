from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    gender = models.CharField(default='Male', max_length=10)
    mobile = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, max_length=200)
    medicine = models.TextField(null=True)
    detail = models.TextField(null=True)
    note = models.TextField(null=True)
    amount = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)

    def __str__(self):
        return self.name
