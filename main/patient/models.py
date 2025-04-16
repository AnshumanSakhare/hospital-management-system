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

class Appointment(models.Model):
    patient_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    contact = models.CharField(max_length=15)
    appointment_date = models.DateField()
    doctor_name = models.CharField(max_length=100)
    reason = models.TextField()
    status = models.CharField(max_length=20, default='Pending')  # Pending, Confirmed, Rejected
    appointment_time = models.TimeField(null=True, blank=True)
    additional_details = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Appointment for {self.patient_name} with Dr. {self.doctor_name} on {self.appointment_date}"
