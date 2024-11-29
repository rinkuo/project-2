from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(unique=True)
    date_birth = models.DateField()
    gender = models.CharField(max_length=6)
    address = models.TextField()


