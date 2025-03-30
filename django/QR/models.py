from django.db import models

# Create your models here.

class Student(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    ]
     
    username = models.CharField(max_length=80) 
    password = models.CharField(max_length=80)
    full_name = models.CharField(max_length=255)
    registration_number = models.CharField(max_length=50, unique=True)
    program = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='none')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Active')
    date_registered = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.full_name} ({self.registration_number})"
