from django.contrib import admin
from django.urls import path
from core.views import VenderAPIView, Purchase_OrderAPIView, Historical_PerformanceAPIView

urlpatterns = [
    path('vender', VenderAPIView.as_view()),
    path('vender/<int:pk>', VenderAPIView.as_view()),
    
    path('Purchase_Order', Purchase_OrderAPIView.as_view()),
    path('Purchase_Order/<int:pk>', Purchase_OrderAPIView.as_view()),
    
    path('api/vendors/<int:vendor_id>/performance/', Historical_PerformanceAPIView.as_view(), name='vendor_performance'),

]

