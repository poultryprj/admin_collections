from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from routes.models import RouteModel
from shops1.models import ShopRoute
from .models import Collection, ShopModel
from .serializers import CollectionSerializer, RouteModelSerializer, ShopModelSerializer
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.




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
        print(request.data['cashierId'])


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




# @api_view(['POST'])
# def UserLogin(request):
#     if request.method == 'POST':
#         user_name = request.data.get('user_name', None)
#         user_password = request.data.get('user_password', None)

#         if not user_name or not user_password:
#             return Response({
#                 "message_text": "Failure",
#                 "message_code": 999,
#                 "message_data": 'Invalid input. Both user_name and user_password are required.'
#             }, status=status.HTTP_400_BAD_REQUEST)

#         try:
#             user = UserModel.objects.get(user_name=user_name, user_password=user_password)

#         except UserModel.DoesNotExist:
#             return Response({
#                 "message_text": "Failure",
#                 "message_code": 999,
#                 "message_data": []
#             }, status=status.HTTP_404_NOT_FOUND)
        
#         if user_password != user.user_password:
#             return Response({"error": "Invalid Password."}, status=status.HTTP_401_UNAUTHORIZED)

#         serializer = UserModelSerializer(user)
        
#         response_data = { 
#             "message_text": "Success",
#             "message_code": 1000,
#             "message_data": [serializer.data]  
#         }
#         return Response(response_data, status=status.HTTP_200_OK)




# *************************************** User LogIn ****************************************

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
                    "message_data": []}, status=405)
    


    
# ********************************************** Get Shops Under Route ************************************************



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
    