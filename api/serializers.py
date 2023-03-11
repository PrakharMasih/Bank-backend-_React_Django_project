from rest_framework import serializers
from api.models import AllCustomers , TransactionHistory

class CustomerSerializers(serializers.HyperlinkedModelSerializer):
    customer_id = serializers.ReadOnlyField()
    class Meta:
        model= AllCustomers
        fields= "__all__"

class TransactionSerializers(serializers.HyperlinkedModelSerializer):
    Transaction_id = serializers.ReadOnlyField()
    class Meta:
        model= TransactionHistory
        fields= "__all__"