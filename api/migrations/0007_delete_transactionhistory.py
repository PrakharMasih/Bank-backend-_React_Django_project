# Generated by Django 4.1 on 2023-03-11 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_rename_customerid_transactionhistory_customer_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TransactionHistory',
        ),
    ]