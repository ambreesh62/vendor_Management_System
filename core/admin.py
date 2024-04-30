from django.contrib import admin
from core.models import Vender, Purchase_Order, Historical_Performance
# Register your models here.

admin.site.register(Vender)
admin.site.register(Purchase_Order)
admin.site.register(Historical_Performance)