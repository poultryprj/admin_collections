
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from routes.models import RouteModel
from shops1.models import ProductIssue, ProductRecieve, ShopRoute
from user.models import UserModel
from vehicle2.models import Vehicle
from .models import Collection, ShopModel, CollectionMode
from .serializers import CollectionSerializer, ProductRecieveSerializer, ShopModelSerializer, CollectionModeSerializer, VehicleSerializer
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from django.utils import timezone
from django.contrib.auth.models import Group
from django.db.models import Sum

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


# @api_view(['GET'])
# def GetShopsUnderRoute(request, route_id):
#     try:
#         shop_routes = ShopRoute.objects.filter(route_id=route_id)
        
#         if not shop_routes.exists():
#             return Response({
#                 "message_text": "Failure",
#                 "message_code": 999,
#                 "message_data": []
#             }, status=404)
        
#         shops_under_route = shop_routes.select_related('shop_id')
#         shop_ids = [shop.shop_id_id for shop in shops_under_route]

#         shops = ShopModel.objects.filter(shop_id__in=shop_ids)
       

#         shops_data = []
#         for shop in shops:
#             shop_data = {
#                 'shopcode': shop.shop_code,
#                 'shopname': shop.shop_name,
#             }
#             shops_data.append(shop_data)


#         response_data = {
#             "message_text": "Success",
#             "message_code": 1000,
#             "message_data": shops_data,
#         }

#         return Response(response_data, status=status.HTTP_200_OK)
    
#     except Exception as e:
#         response_data = {
#             "message_text": str(e),
#             "message_code": 999,
#             "message_data": {},
#         }
#         return Response(response_data, status=500)



@api_view(['GET'])
def GetShopsUnderRoute(request, route_id, shop_code=None):
    try:
        shop_routes = ShopRoute.objects.filter(route_id=route_id)

        if not shop_routes.exists():
            return Response({
                "message_text": "Failure",
                "message_code": 999,
                "message_data": []
            }, status=404)

        if shop_code:
            # If shop_code is provided, filter shops based on the code
            shops = ShopModel.objects.filter(shop_code=shop_code)
            serializer = ShopModelSerializer(ShopModel, many=True)
            response_data = {
            "message_text": "Success",
            "message_code": 1000,
            "message_data": serializer.data,
        }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            # If shop_code is not provided, continue with existing logic
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

    except ShopModel.DoesNotExist:
        return Response({
            "message_text": "Shop not found",
            "message_code": 404,
            "message_data": [],
        }, status=404)



# ****************************************************************


@api_view(['GET'])
def UserListByGroup(request):
    try:
        group_name = request.data.get('group_name', 'all')
        print(group_name)
        if group_name == 'all':
            users = User.objects.all()
        else:
            users = User.objects.filter(groups__name=group_name)
        
        users_data = []
        for user in users:
            user_data = {
                "user_id": user.id,
                "user_mobile_number": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name,
            }
            users_data.append(user_data)

        response_data = {
            "message_text": "Success",
            "message_code": 1000,
            "message_data": users_data,
        }
        return Response(response_data, status=status.HTTP_200_OK)
    except Group.DoesNotExist:
        return Response({
            "message_text": "Failure",
            "message_code": 999,
            "message_data": []
        }, status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def GroupList(request):
    groups = Group.objects.all()

    groups_data = []
    for group in groups:
        group_data = {
            "role_id":group.id,
            "role_name": group.name,
        }
        groups_data.append(group_data)

    response_data = {
    "message_text": "Success",
    "message_code": 1000,
    "message_data": groups_data,
}
    return Response(response_data, status=status.HTTP_200_OK)



@api_view(['GET'])
def vehicleList(request):
    try:
        vehicles = Vehicle.objects.all()

        vehicles_data = []
        for vehicle in vehicles:
            vehicle_data = {
                "vehicle_id":vehicle.vehicle_id,
                "registration_no": vehicle.registration_no,
                "owner_name" : vehicle.owner_name,
                "vehicle_company": vehicle.vehicle_make_Id.vehicle_make_by
            }
            vehicles_data.append(vehicle_data)

        response_data = {
            "message_text": "Success",
            "message_code": 1000,
            "message_data": vehicles_data,
        }
        return Response(response_data, status=status.HTTP_200_OK)
    except Vehicle.DoesNotExist:
        return Response({
                "message_text": "Failure",
                "message_code": 999,
                "message_data": []
            }, status=status.HTTP_404_NOT_FOUND)




@api_view(['GET'])
def ReceivedProductsByDate(request):
    date = request.data.get('date')
    print(date)
    try:
        products = ProductRecieve.objects.filter(recieved_date=date)
        serializer = ProductRecieveSerializer(products, many=True)
        # total_amount = products.aggregate(Sum('amount'))['amount__sum']

        products_data = []
        for product in products:
            product_data = {
                "product_record_id":product.product_record_id,
                "recieved_date": product.recieved_date,
                "vendor_name" : product.vendorId.vendor_name,
                "product_type": product.product_typeId.product_type,
                "recieved_quantity": product.recieved_quantity,
                "recieved_weight":product.recieved_weight
            }
            products_data.append(product_data)

        response_data = {
            "message_text": "Success",
            "message_code": 1000,
            "message_data": products_data
            # {
            #     "products": 
            #     # "total_amount": total_amount,
            # },
        }
        return Response(response_data, status=status.HTTP_200_OK)
    except ProductRecieve.DoesNotExist:
        return Response({
                "message_text": "Failure",
                "message_code": 999,
                "message_data": []
            }, status=status.HTTP_404_NOT_FOUND)
    


@api_view(['GET'])
def IssueProductsByDate(request):
    date = request.data.get('date')
    try:
        issues = ProductIssue.objects.filter(issue_date=date)

        issue_products_data = []
        for issue in issues:
            issue_product_data = {
                "product_issue_id":issue.product_issue_id,
                "issue_date": issue.issue_date,
                "shop_name" : issue.shopId.shop_name,
                "issue_amount": issue.issue_amount,
                "product_type": issue.product_typeId.product_type
            }
            issue_products_data.append(issue_product_data)

        response_data = {
            "message_text": "Success",
            "message_code": 1000,
            "message_data": issue_products_data,
           
        }
        return Response(response_data, status=status.HTTP_200_OK)
    except ProductIssue.DoesNotExist:
        return Response({
            "message_text": "Failure",
            "message_code": 999,
            "message_data": "No products issued on this date",
        }, status=status.HTTP_404_NOT_FOUND)





@api_view(['GET'])
def IssueProductsByDateDriverVechicle(request):
    date = request.data.get('date')
    driver_id = request.data.get('driver_id')
    vehicle_id = request.data.get('vehicle_id')
    
    if not all([date, driver_id, vehicle_id]):
        return Response({
            "message": "Failure",
            "message_code": 999,
            "message_data": "Missing parameters"
        }, status=400)

    try:
        issuesProduct = ProductIssue.objects.get(issue_date=date, driverId=driver_id, vehicleId=vehicle_id)
       
        issuesProducts = {
                "product_issue_id": issuesProduct.product_issue_id,
                "issue_date": issuesProduct.issue_date,
                "shop_name": issuesProduct.shopId.shop_name,
                "vehicleId": issuesProduct.vehicleId.owner_name,
                "driverId": issuesProduct.driverId.user_name,
                "product_type": issuesProduct.product_typeId.product_type,
              
        }

        response_data = {
            "message_text": "Success",
            "message_code": 1000,
            "message_data": issuesProducts,
           
        }
        return Response(response_data, status=status.HTTP_200_OK)
    
    except ProductIssue.DoesNotExist:
        return Response({
            "message_text": "Failure",
            "message_code": 999,
            "message_data": "No products issued on this date",
        }, status=status.HTTP_404_NOT_FOUND)

