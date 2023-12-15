from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Collection, ShopModel
from .serializers import CollectionSerializer, ShopModelSerializer
from django.db.models import Q
from django.contrib.auth.models import User


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
        required_fields = ['collection_date', 'collection_time', 'shopId', 'cashierId', 'latitude', 'longtitude', 'total_amount', 'fanialize_by']
        missing_fields = []

        for field in required_fields:
            if field not in request.data:
                missing_fields.append(field)

        if missing_fields:
            return Response({
                "message_text": f"Missing fields: {', '.join(missing_fields)}",
                "message_code": 998,
                "message_data": [],
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            serializer = CollectionSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                response_data = {
                    "message_text": "Success",
                    "message_code": 1000,
                    "message_data": serializer.data
                }
                return Response(response_data, status=status.HTTP_201_CREATED)
            else:
                return Response({
                    "message_text": "Validation error",
                    "message_code": 997,
                    "message_data": serializer.errors,
                }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                "message_text": "An error occurred",
                "message_code": 996,
                "message_data": str(e),
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['GET'])
def CollectionView(request):
    if request.method == 'GET':
        cashier_id = request.GET.get('cashierId')
        if cashier_id:
            # Validate if cashierId is an integer
            if not cashier_id.isdigit():
                return Response({
                    "message_text": "Invalid cashierId format. Must be an integer.",
                    "message_code": 997,
                    "message_data": []
                }, status=status.HTTP_400_BAD_REQUEST)

            # Check if the cashierId exists in the database
            try:
                cashier = User.objects.get(id=cashier_id)
            except User.DoesNotExist:
                return Response({
                    "message_text": "CashierId does not exist",
                    "message_code": 996,
                    "message_data": []
                }, status=status.HTTP_404_NOT_FOUND)

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
