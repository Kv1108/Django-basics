from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone_no = models.IntegerField(null = True)    
    joining_date = models.DateField(null = True)

