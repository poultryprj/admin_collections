
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from routes.models import RouteModel
from shops1.models import ShopRoute
from .models import Collection, Complaint, ShopModel, CollectionMode, SkipShop
from .serializers import CollectionSerializer, ComplaintSerializer, ShopModelSerializer, CollectionModeSerializer, SkipShopSerializer
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
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


# *********************************************************** All Route List ***********************************************

@api_view(['GET'])
def RoutesList(request):
    if request.method == 'GET':
        routes = RouteModel.objects.all()
        routes_data = []
        for route in routes:
            route_data = {
                'route_title': route.route_id,
                'route_info': route.route_name,
            }
            routes_data.append(route_data)

        response_data = {
            "message_text": "Success",
            "message_code": 1000,
            "message_data": routes_data,
        }
        return Response(response_data)
    
    else:
        return Response({
                    "message_text": "Failure",
                    "message_code": 999,
                    "message_data": [],
                }, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def UserLogin(request):
    if request.method == 'POST':
        user_mobile_number = request.data.get('user_mobile_number', None)
        user_pin = request.data.get('user_pin', None)

        if not user_mobile_number or not user_pin:
            return Response({
                "message": "Invalid input. Both username and password are required."
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = authenticate(username=user_mobile_number, password=user_pin)
           
            if user is not None:
                # Authentication successful, return user data
                response_data = { 
                    "message_text": "Success",
                    "message_code": 1000,
                    "message_data": {
                        "user_id":user.id,
                        "user_mobile_number": user.username,
                        "first_name":user.first_name,
                        "last_name":user.last_name,

                    }
                }
                
                return Response(response_data, status=status.HTTP_200_OK)
            else:
                return Response({
                    "message_text": "Failure",
                    "message_code": 999,
                    "message_data": {}
                }, status=status.HTTP_401_UNAUTHORIZED)

        except Exception as e:
            return Response({
                    "message_text": "Failure",
                    "message_code": 999,
                    "message_data": {}
                }, status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response({'message': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
def GetShopsUnderRoute(request, route_id):
    try:
        shop_routes = ShopRoute.objects.filter(route_id=route_id)
        
        if not shop_routes.exists():
            return Response({
                "message_text": "Failure",
                "message_code": 999,
                "message_data": []
            }, status=404)
        
        shops_under_route = shop_routes.select_related('shop_id')
        shop_ids = [shop.shop_id_id for shop in shops_under_route]

        shops = ShopModel.objects.filter(shop_id__in=shop_ids)
       

        shops_data = []
        for shop in shops:
            shop_data = {
                'shopcode': shop.shop_code,
                'shopname': shop.shop_name,
            }
            shops_data.append(shop_data)


        response_data = {
            "message_text": "Success",
            "message_code": 1000,
            "message_data": shops_data,
        }

        return Response(response_data, status=status.HTTP_200_OK)
    
    except Exception as e:
        response_data = {
            "message_text": str(e),
            "message_code": 999,
            "message_data": {},
        }
        return Response(response_data, status=500)


########################################### SkipShop ########################################################
########## skip shop add ###########
@api_view(['POST'])
def SkipShopAdd(request):
    if request.method == 'POST':
        required_fields = ['skip_shop_date', 'skip_shop_time', 'shopId', 'cashierId', 'approve_yn', 'remark', 'approve_byId', 'created_on', 'created_by']
        missing_fields = [field for field in required_fields if field not in request.data]

        if missing_fields:
            return Response({
                "message_text": f"Missing fields: {', '.join(missing_fields)}",
                "message_code": 998,
                "message_data": [],
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            serializer = SkipShopSerializer(data=request.data)
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


############## Skip Shop View Data By Cashier Id ####################
@api_view(['GET'])
def SkipShopListView(request):
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

            # Fetch skip shop data associated with the provided cashier ID
            collections = SkipShop.objects.filter(cashierId=cashier_id)
            serializer = SkipShopSerializer(collections, many=True)
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



########################################### Complaint ########################################################
########## Complaint Add ###########
@api_view(['POST'])
def ComplaintAdd(request):
    if request.method == 'POST':
        required_fields = ['complaint_date', 'complaint_time', 'shopId', 'cashierId', 'approve_yn', 'remark', 'approve_byId', 'created_on', 'created_by']
        missing_fields = [field for field in required_fields if field not in request.data]

        if missing_fields:
            return Response({
                "message_text": f"Missing fields: {', '.join(missing_fields)}",
                "message_code": 998,
                "message_data": [],
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            serializer = ComplaintSerializer(data=request.data)
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


############## Complaint List View by cashier Id ####################
@api_view(['GET'])
def ComplaintListView(request):
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

            # Fetch skip shop data associated with the provided cashier ID
            collections = Complaint.objects.filter(cashierId=cashier_id)
            serializer = ComplaintSerializer(collections, many=True)
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