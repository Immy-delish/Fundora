# loans/admin.py
from django.contrib import admin
from .models import Client, Loan, Repayment

admin.site.register(Client)
admin.site.register(Loan)
admin.site.register(Repayment)
