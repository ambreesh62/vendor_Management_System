from django.shortcuts import render
from core.models import Vender, Purchase_Order, Historical_Performance
from core.serializers import VanderSerializer, Purchase_OrderSerializer, Historical_Performance
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status




# Create your views here.

class VenderAPIView(APIView):
    def post(self, request):
        serilalizer = VanderSerializer(data=request.data)
        if not serilalizer.is_valid():
            print(serilalizer.errors)
            return Response({'errors' : serilalizer.errors, 'massage' : 'somthing went worng'}, status=status.HTTP_400_BAD_REQUEST)
        serilalizer.save()
        return Response({'playload' : serilalizer.data, 'massage' : 'data saved'}, status=status.HTTP_201_CREATED)
    
    
    def get(self, request):
        vender_objs = Vender.objects.all()
        serializer = VanderSerializer(vender_objs, many=True)
        return Response({'playload' : serializer.data}, status=status.HTTP_200_OK)
