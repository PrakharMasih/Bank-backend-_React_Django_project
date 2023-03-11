from django.contrib import admin
from django.urls import path ,include
from api.views import CustomerViewset , TransactionViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'customer', CustomerViewset)
router.register(r'transactionhistory', TransactionViewset)

urlpatterns = [
    path('', include(router.urls)),
]