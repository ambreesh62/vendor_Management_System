from django.shortcuts import render
from core.models import Vender, Purchase_Order, Historical_Performance
from core.serializers import VanderSerializer, Purchase_OrderSerializer, Historical_Performance
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status




# Vender APIViews here.

class VenderAPIView(APIView):
    def post(self, request):
        serilalizer = VanderSerializer(data=request.data)
        if not serilalizer.is_valid():
            print(serilalizer.errors)
            return Response({'errors' : serilalizer.errors, 'massage' : 'somthing went worng'}, status=status.HTTP_400_BAD_REQUEST)
        serilalizer.save()
        return Response({'playload' : serilalizer.data, 'massage' : 'Your data saved'}, status=status.HTTP_201_CREATED)
    
    
    def get(self, request, pk=None):
        
        if pk:
            vender_objs = Vender.objects.get(id=pk)
            serializer = VanderSerializer(vender_objs)
            return Response({'massage': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)
        
        vender_objs = Vender.objects.all()
        serializer = VanderSerializer(vender_objs, many=True)
        return Response({'playload' : serializer.data}, status=status.HTTP_200_OK)
    
    def put(self, request, pk=None):
        
        try:
            
            vender_objs = Vender.objects.get(pk=pk)
            seralizer = VanderSerializer(vender_objs, data=request.data)
            
            if not seralizer.is_valid():
                print(seralizer.errors)
                return Response({'errors' : seralizer.errors, 'massage' : 'somthing went worng'}, status=status.HTTP_400_BAD_REQUEST)
            seralizer.save()
            return Response({'playload' : seralizer.data,}, status=status.HTTP_202_ACCEPTED)

        except Vender.DoesNotExist:
            return Response({'massage' : 'DoesNotExist'}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk=None):
        
        try:
            vender_objs = Vender.objects.get(pk=pk)
            vender_objs.delete()
            return Response({'massage' : 'Data has been deleted'})
        except Vender.DoesNotExist:
            return Response({'massage' : 'DoesNotExist'}, status=status.HTTP_400_BAD_REQUEST)    
