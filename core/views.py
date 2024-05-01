from django.shortcuts import render
from core.models import Vender, Purchase_Order, Historical_Performance
from core.serializers import VanderSerializer, Purchase_OrderSerializer, Historical_Performance
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status




# Vender APIViews here.

class VenderAPIView(APIView):
    def post(self, request):
        serializer = VanderSerializer(data=request.data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'errors' : serializer.errors, 'massage' : 'somthing went worng'}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({'massage' : 'Your data saved', 'data' : serializer.data}, status=status.HTTP_201_CREATED)
    
    
    def get(self, request, pk=None):
        
        if pk:
            vender_objs = Vender.objects.get(id=pk)
            serializer = VanderSerializer(vender_objs)
            return Response({'massage': 'success', 'data': serializer.data}, status=status.HTTP_202_ACCEPTED)
        
        vender_objs = Vender.objects.all()
        serializer = VanderSerializer(vender_objs, many=True)
        return Response({'playload' : serializer.data}, status=status.HTTP_200_OK)
    
    def put(self, request, pk=None):
        
        try:
            
            vender_objs = Vender.objects.get(pk=pk)
            serializer = VanderSerializer(vender_objs, data=request.data)
            
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'errors' : serializer.errors, 'massage' : 'somthing went worng'}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response({'playload' : serializer.data,}, status=status.HTTP_202_ACCEPTED)

        except Vender.DoesNotExist:
            return Response({'massage' : 'DoesNotExist'}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk=None):
        
        try:
            vender_objs = Vender.objects.get(pk=pk)
            vender_objs.delete()
            return Response({'massage' : 'Data has been deleted'})
        except Vender.DoesNotExist:
            return Response({'massage' : 'DoesNotExist'}, status=status.HTTP_400_BAD_REQUEST)    


# Purchase_Order APIViews here.

class Purchase_OrderAPIView(APIView):
    def post(self, request):
        serializer = Purchase_OrderSerializer(data=request.data)
        
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'errors' : serializer.errors, 'massage' : 'somthing went worng'}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({'massage' : 'Your data is saved', 'data' : serializer.data}, status=status.HTTP_201_CREATED)
    
    
    def get(self,request, pk=None):
        
        if pk:
            purchase_objs = Purchase_Order.objects.get(pk=pk)
            serializer = Purchase_OrderSerializer(purchase_objs)
            return Response({'massage' : 'success', 'data' : serializer.data}, status=status.HTTP_202_ACCEPTED)
        purchase_objs = Purchase_Order.objects.all()
        serializer = Purchase_OrderSerializer(purchase_objs, many=True)
        return Response({'playload' : serializer.data,}, status=status.HTTP_200_OK)
    
    def put (self, request, pk=None):
        
        try:
            purchase_objs = Purchase_Order.objects.get(pk=pk)
            serializer = Purchase_OrderSerializer(purchase_objs, data=request.data)
            
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'errors' : serializer.errors, 'massage' : 'somthing went worng'}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response({'Playload' : serializer.data, 'massage' : 'Your data is saved'}, status=status.HTTP_202_ACCEPTED)
        except Purchase_Order.DoesNotExist:
            return Response({'massage' : 'DoesNotExist'}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, requesr, pk=None):
        try:
            purchase_objs = Purchase_Order.objects.get(pk=pk)
            purchase_objs.delete()
            return Response({'massage' : 'Data has been deleted'}, status=status.HTTP_200_OK)
        except Purchase_Order.DoesNotExist:
            return Response({'massage' : 'DoesNotExist'}, status=status.HTTP_400_BAD_REQUEST)