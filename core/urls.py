from django.contrib import admin
from django.urls import path
from core.views import VenderAPIView, Purchase_OrderAPIView
urlpatterns = [
    path('vender', VenderAPIView.as_view()),
    path('vender/<int:pk>', VenderAPIView.as_view()),
    
    path('Purchase_Order', Purchase_OrderAPIView.as_view()),
    path('Purchase_Order/<int:pk>', Purchase_OrderAPIView.as_view()),
]

