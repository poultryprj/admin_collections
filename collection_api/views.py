import datetime
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Collection, CollectionMode, ShopModel
from .serializers import CollectionModeSerializer, CollectionSerializer, ShopModelSerializer
from django.db.models import Q
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import CollectionMode
import datetime
from django.utils import timezone


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
        

@api_view(['POST'])
def CollectionModeAdd(request):
    if request.method == 'POST':
        try:
            user_id = request.data.get('user_id')
            collection_id = request.data.get('collectionId')
            payment_mode = request.data.get('payment_mode')
            payment_amount = request.data.get('payment_amount')
            upload_image = request.FILES.get('upload_image')

            if collection_id and payment_mode and payment_amount and upload_image:
                collection = Collection.objects.get(pk=collection_id)
                collection_mode = CollectionMode(
                    collectionId=collection,
                    payment_mode=payment_mode,
                    payment_amount=payment_amount
                )
                
                # Generate the custom filename
                ShopModelData = ShopModel.objects.first() 
                
                current_datetime = timezone.now()
                original_photo_name = upload_image.name
                custom_filename = f"{payment_mode}_{user_id}_{ShopModelData.shop_id}_{current_datetime.strftime('%Y%m%d_%H%M%S')}_{original_photo_name}"
                
                # Save the file with the custom filename in the specified folder within the bucket
                file_content = ContentFile(upload_image.read())
                collection_mode.upload_image.save(custom_filename, file_content)
                
                response_data = {
                    "message_text": "Success",
                    "message_code": 1000,
                    "message_data": {
                        "file_url": collection_mode.upload_image.url  # Assuming you need to retrieve the uploaded file URL
                    }
                }
                return Response(response_data, status=status.HTTP_201_CREATED)
            else:
                return Response({
                    "message_text": "Validation error",
                    "message_code": 997,
                    "message_data": "Invalid data provided",
                }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                "message_text": "An error occurred",
                "message_code": 996,
                "message_data": str(e),
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def CollectionModeGet(request, collection_id):
    try:
        collection = Collection.objects.get(pk=collection_id)
        collection_modes = CollectionMode.objects.filter(collectionId=collection)

        serializer = CollectionModeSerializer(collection_modes, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Collection.DoesNotExist:
        return Response({
            "message_text": "Collection not found",
            "message_code": 404,
            "message_data": f"Collection with ID {collection_id} does not exist",
        }, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({
            "message_text": "An error occurred",
            "message_code": 500,
            "message_data": str(e),
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
