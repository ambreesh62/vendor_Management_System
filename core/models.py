from django.db import models
from base.models import BaseModel

# Create your models here.

class Vender(BaseModel):
    name = models.CharField(("Vendor's name"), max_length=50)
    contact_details = models.TextField(("Contact information of the vendor"))
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField(
        verbose_name="On-time Delivery Rate",
        help_text="Tracks the percentage of on-time deliveries."
    )
    quality_rating_avg = models.FloatField(
        verbose_name="Quality Rating Average",
        help_text="Average rating of quality based on purchase orders."
    )
    average_response_time = models.FloatField(
        verbose_name="Average Response Time",
        help_text="Average time taken to acknowledge purchase orders."
    )
    fulfillment_rate = models.FloatField(
        verbose_name="Fulfillment Rate",
        help_text="Percentage of purchase orders fulfilled successfully."
    )

    def __str__(self):
        return f"Vender - {self.pk}"
    
    
    
    
    
class Purchase_Order(BaseModel):
    status_choices = [
    ('pending', 'Pending'),
    ('completed', 'Completed'),
    ('canceled', 'Canceled'),
    ]
    po_number = models.CharField(max_length=50, unique=True)
    vendor = models.ForeignKey(Vender,on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateField()
    items = models.JSONField()
    quantity = models.IntegerField(null=False)
    status = models.CharField(max_length=20, choices=status_choices)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField(auto_now_add=True)
    acknowledgment_date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"PO - {self.pk} - {self.get_status_display()}"
    
    
    


class Historical_Performance(BaseModel):