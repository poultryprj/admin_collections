from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from route.models import RouteModel
from shop.models import ProductIssue, ProductRecieve, ShopBalance, ShopOwner, ShopRoute
from vehicle.models import Vehicle
from .models import Collection, Complaint, ShopModel, CollectionMode, SkipShop 
from .serializers import CollectionSerializer, ComplaintSerializer, ProductIssueSerializer, ProductRecieveSerializer, ShopModelSerializer, CollectionModeSerializer, SkipShopSerializer, VehicleRunningSerializer, VehicleSerializer
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from django.utils import timezone
from django.contrib.auth.models import Group
from django.db.models import Sum
from django.db.models import Max
from django.db.models import F
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from .serializers import ShopProductRequestSerializer
import random
import requests

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

########## Collection Mode Add With OTP DATA SAVE in DATABASE        
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
                
                ShopModelData = ShopModel.objects.first() 
                
                current_datetime = timezone.now()
                original_photo_name = upload_image.name
                custom_filename = f"{payment_mode}_{user_id}_{ShopModelData.shop_id}_{current_datetime.strftime('%Y%m%d_%H%M%S')}_{original_photo_name}"
                
                file_content = ContentFile(upload_image.read())
                collection_mode.upload_image.save(custom_filename, file_content)
                
                # Generate 4-digit OTP
                otp = ''.join(random.choices('0123456789', k=4))

                # Save the OTP in the CollectionMode model
                collection_mode.OTP = otp
                collection_mode.save()
                
                # Construct the message with OTP
                message = f"Your OTP for the transaction is: {otp}"
                
                # Assuming the shop owner's number is fetched dynamically

                shop_owner_number = ShopModelData.shop_ownerId.owner_contactNo
                print(shop_owner_number)
                
                # Construct the WhatsApp message URL with parameters
                whatsapp_url = f"https://wts.vision360solutions.co.in/api/sendText?token=63944323e575be8d4fc95a50&phone={shop_owner_number}&Text={message}"
                
                # Make an HTTP GET request to send the WhatsApp message
                response = requests.get(whatsapp_url)

                if response.status_code == 200:
                    # Formulate your response data
                    serialized_data = CollectionModeSerializer(collection_mode).data
                    response_data = {
                        "message_text": "Success",
                        "message_code": 1000,
                        "message_data": {
                            "file_url": serialized_data['upload_image'],  
                            "otp": otp
                        }
                    }
                    return Response(response_data, status=status.HTTP_201_CREATED)
                else:
                    return Response({
                        "message_text": "Failed to send WhatsApp message",
                        "message_code": 998,
                        "message_data": "Failed to send OTP to shop owner",
                    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
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


########## OTP VErification 
@api_view(['POST'])
def OTPVerification(request):
    if request.method == 'POST':
        try:
            collection_id = request.data.get('collection_id')
            OTP = request.data.get('OTP')
            collection_data = CollectionMode.objects.filter(collectionId=collection_id, OTP=OTP)
            
            if collection_data.exists():
                response_data = {
                    "message_text": "Success",
                    "message_code": 1000,
                    "message_data": f"Your OTP : {OTP} Is Verifified Successful..!!"
                }
                return Response(response_data, status=status.HTTP_200_OK)
            else:
                return Response({
                    "message_text": "Failure",
                    "message_code": 997,
                    "message_data": "Invalid OTP or collection ID",
                }, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(e)
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
            # Get the count of shops for each route
            shop_count = ShopRoute.objects.filter(route_id=route.route_id).count()
            
            route_data = {
                'route_title': route.route_id,
                'route_info': route.route_name,
                'shop_count': shop_count,  # Include the shop count in the route data
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
        user_role = request.data.get('user_role', None)  

        if not user_mobile_number or not user_pin or not user_role:
            return Response({
                "message": "Invalid input. User mobile number, pin, and user role are required."
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = authenticate(username=user_mobile_number, password=user_pin)
           
            if user is not None:
                if Group.objects.filter(name=user_role, user=user).exists():
                    response_data = { 
                        "message_text": "Success",
                        "message_code": 1000,
                        "message_data": {
                            "user_id": user.id,
                            "user_mobile_number": user.username,
                            "first_name": user.first_name,
                            "last_name": user.last_name,
                            "user_role": user_role  
                        }
                    }
                    return Response(response_data, status=status.HTTP_200_OK)
                else:
                    return Response({
                        "message_text": f"User role '{user_role}' does not exist for the given username.",
                        "message_code": 999,
                        "message_data": {}
                    }, status=status.HTTP_401_UNAUTHORIZED)
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
                "message_text": "No shops found for this route",
                "message_code": 404,
                "message_data": []
            }, status=status.HTTP_404_NOT_FOUND)

        # Get the shop IDs under the given route
        shop_ids = shop_routes.values_list('shop_id_id', flat=True)

        # Fetch all shops under the given route
        shops = ShopModel.objects.filter(shop_id__in=shop_ids)

        # Fetch latest balances for shops under the route
        latest_balances = ShopBalance.objects.filter(
            shopId_id__in=shop_ids,
            is_deleted=False
        ).values('shopId_id').annotate(recent_balance_date=Max('balance_date'))

        # Create a dictionary to store the latest balance for each shop
        shop_balances = {
            balance['shopId_id']: balance['recent_balance_date']
            for balance in latest_balances
        }

        shops_data = []
        for shop in shops:
            shop_data = {
                'shopcode': shop.shop_code,
                'shopname': shop.shop_name,
                'out_standing_amount': 0  # Default to 0 for all shops
            }

            # Check if shop has a recent balance, update outstanding amount if available
            recent_balance_date = shop_balances.get(shop.shop_id)
            if recent_balance_date:
                recent_balance = ShopBalance.objects.filter(
                    shopId_id=shop.shop_id,
                    balance_date=recent_balance_date,
                    is_deleted=False
                ).first()

                if recent_balance:
                    shop_data['out_standing_amount'] = recent_balance.balance

            shops_data.append(shop_data)

        total_shop_count = len(shops_data)

        response_data = {
            "message_text": "Success",
            "message_code": 200,
            "message_data": {
                'total_shop_count': total_shop_count,
                'shops': shops_data
            }
        }

        return Response(response_data, status=status.HTTP_200_OK)

    except Exception as e:
        response_data = {
            "message_text": str(e),
            "message_code": 500,
            "message_data": {},
        }
        return Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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

# ****************************************************************
@api_view(['GET'])
def UserListByGroup(request):
    try:
        group_name = request.query_params.get('group_name', 'all')  # Use query_params for GET request
        print(group_name)
        if group_name == 'all':
            users = User.objects.all()
        else:
            users = User.objects.filter(groups__name=group_name)
        
        users_data = []
        for user in users:
            user_groups = list(user.groups.values_list('name', flat=True))  # Fetch user's group names
            user_data = {
                "user_id": user.id,
                "user_mobile_number": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "user_roles": user_groups,  # Include user roles in the response
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


@api_view(['GET'])
def ApproveCollection(request):
    collection_date = request.data.get('collection_date')
    cashier_id = request.data.get('cashierId')

    if collection_date and cashier_id:
        try:
            
            collection_instances = Collection.objects.filter(
                collection_date=collection_date,
                cashierId=cashier_id,
                collections_status='0'  
            )

            if not collection_instances.exists():
                return Response({
                    "message_text": "No pending collections found for the given criteria.",
                    "message_code": 404,
                    "message_data": []
                }, status=status.HTTP_404_NOT_FOUND)

         
            fanalize_data = []
            cashier_user = User.objects.get(pk=cashier_id)

            for collection_instance in collection_instances:
                collection_instance.collections_status = '1'
                collection_instance.fanialize_by = cashier_user
                collection_instance.save()

                shop_id = collection_instance.shopId.shop_name
                amount = collection_instance.total_amount
                collection_status = collection_instance.collections_status


                data = {
                    "Shop Name":shop_id,
                    "Amount": amount,
                    "Finalize Status" : collection_status
                }
                fanalize_data.append(data)

            response_data = {
                "message_text": "Success",
                "message_code": 1000,
                "message_data":fanalize_data
            }
            return Response(response_data, status=status.HTTP_200_OK)

        except Collection.DoesNotExist:
            return Response({
                "message_text": "Failure",
                "message_code": 999,
                "message_data": "Collection not found.",
            }, status=status.HTTP_404_NOT_FOUND)

        except User.DoesNotExist:
            return Response({'message': 'Cashier not found.'}, status=status.HTTP_404_NOT_FOUND)

    return Response({'message': 'Invalid or missing parameters.'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def GetShopCollections(request):
    shop_id = request.data.get('shop_id')
    cashier_id = request.data.get('cashier_id')
    collection_date = request.data.get('collection_date')

    collections = Collection.objects.filter(
        shopId=shop_id,
        cashierId=cashier_id,
        collection_date=collection_date,
        collections_status='0'  
    )

    if not collections.exists():
        response_data = {
            "message_text": "No data found for the given criteria.",
            "message_code": 404,
            "message_data": []  
        }
        return Response(response_data, status=status.HTTP_404_NOT_FOUND)

    collection_modes = CollectionMode.objects.filter(collectionId__in=collections)

    if not collection_modes.exists():
        response_data = {
            "message_text": "No payment modes found for the given criteria.",
            "message_code": 404,
            "message_data": []  
        }
        return Response(response_data, status=status.HTTP_404_NOT_FOUND)

    payment_modes_amounts = collection_modes.values('payment_mode', ).annotate(total_amount=Sum('payment_amount'), collection_status=F('collectionId__collections_status'))

    response_data = {
        "message_text": "Success",
        "message_code": 1000,
        "message_data":payment_modes_amounts
    }
    return Response(response_data, status=status.HTTP_200_OK)


@api_view(['POST'])
def AddProductReceive(request):
    try:
        serializer = ProductRecieveSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

            response_data = {
            "message_text": "Success",
            "message_code": 1000,
            "message_data":serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        
    except ValidationError as e:
        return Response({
                "message_text": "Failure",
                "message_code": 999,
                "message_data": str(e),
            }, status=status.HTTP_400_BAD_REQUEST)
       
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    



@api_view(['POST'])
def AddProductIssue(request):
    try:
        serializer = ProductIssueSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

            response_data = {
            "message_text": "Success",
            "message_code": 1000,
            "message_data":serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        
    except ValidationError as e:
       return Response({
                "message_text": "Failure",
                "message_code": 999,
                "message_data": str(e),
            }, status=status.HTTP_400_BAD_REQUEST)
    
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    


@api_view(['POST'])
def AddVehicleRunning(request):
    try:
        serializer = VehicleRunningSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

            response_data = {
            "message_text": "Success",
            "message_code": 1000,
            "message_data":serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        
    except ValidationError as e:
          return Response({
                "message_text": "Failure",
                "message_code": 999,
                "message_data": str(e),
            }, status=status.HTTP_400_BAD_REQUEST)
    
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

########### Shop App API ##############

@api_view(['POST'])
def CreateShopProductRequest(request):
    try:
        serializer = ShopProductRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def GetProductIssuesByDate(request):
    issue_date = request.query_params.get('issue_date')
    if not issue_date:
        return Response("Issue date parameter is missing.", status=status.HTTP_400_BAD_REQUEST)

    product_issues = ProductIssue.objects.filter(issue_date=issue_date)
    if not product_issues.exists():
        return Response("No data found for the given issue date.", status=status.HTTP_404_NOT_FOUND)

    # Group data shopID-wise and then product-wise
    data = {}
    for issue in product_issues:
        shop_id = issue.shopId_id
        product_id = issue.product_typeId_id

        if shop_id not in data:
            data[shop_id] = {}

        if product_id not in data[shop_id]:
            data[shop_id][product_id] = []

        serialized_data = ProductIssueSerializer(issue).data
        data[shop_id][product_id].append(serialized_data)

    return Response(data, status=status.HTTP_200_OK)     ### in the output shopId first key AND second key product_typeId

