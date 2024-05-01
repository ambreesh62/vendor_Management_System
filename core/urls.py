from django.contrib import admin
from django.urls import path
from core.views import VenderAPIView
urlpatterns = [
    path('vender', VenderAPIView.as_view()),
    path('vender/<int:pk>', VenderAPIView.as_view())
]

