from rest_framework import serializers
from core.models import Vendor, Purchase_Order, Historical_Performance
from django.contrib.auth.models import User

class VandorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'
        
        
class Purchase_OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase_Order
        
        fields = '__all__'
        
        
class Historical_PerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historical_Performance
        fields = '__all__' 