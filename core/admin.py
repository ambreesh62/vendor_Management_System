from django.contrib import admin
from core.models import Vendor, Purchase_Order, Historical_Performance
# Register your models here.

admin.site.register(Vendor)
admin.site.register(Purchase_Order)
admin.site.register(Historical_Performance)