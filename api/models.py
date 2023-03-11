from django.db import models

# Create your models here.


class AllCustomers(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    acc_no = models.IntegerField()
    balance = models.IntegerField()


class TransactionHistory(models.Model):
    Transaction_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    name = models.CharField(max_length=50)
    email = models.EmailField()
    acc_no = models.IntegerField()
    balance = models.IntegerField()
