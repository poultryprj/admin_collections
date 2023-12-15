from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Collection, ShopModel
from .serializers import CollectionSerializer, ShopModelSerializer
from django.db.models import Q


@api_view(['GET'])
def ShopModelListView(request):
    if request.method == 'GET':
        users = ShopModel.objects.all()
        print(users)
        serializer = ShopModelSerializer(users, many=True)
        response_data = {
                "message_text": "Success",
                "message_code": 1000,
                "message_data": serializer.data
        }
        return Response(response_data, status=status.HTTP_200_OK)


@api_view(['POST'])
def CollectionsAddView(request):
    if request.method == 'POST':

        serializer = CollectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                "message_text": "Success",
                "message_code": 1000,
                "message_data": serializer.data
        }
            return Response(response_data, status=status.HTTP_201_CREATED)
        
        return Response({
                    "message_text": "Failure",
                    "message_code": 999,
                    "message_data": [],
                }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def CollectionView(request):
    if request.method == 'GET':
        cashier_id = request.GET.get('cashierId')
        if cashier_id:
            collections = Collection.objects.filter(cashierId=cashier_id)
            serializer = CollectionSerializer(collections, many=True)
            response_data = {
                "message_text": "Success",
                "message_code": 1000,
                "message_data": serializer.data
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response({
                "message_text": "No cashierId provided",
                "message_code": 998,
                "message_data": []
            }, status=status.HTTP_400_BAD_REQUEST)
