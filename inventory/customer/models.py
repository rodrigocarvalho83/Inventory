from django.db import models

# Create your models here.


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=15)
    primary_contact_name = models.CharField(max_length=24)
    primary_contact_position = models.CharField(max_length=25)
    primary_contact_department = models.CharField(max_length=15)
    primary_contact_phone = models.CharField(max_length=17)
    primary_contact_email = models.CharField(max_length=30)

    def __str__(self):
        return self.customer_name
