from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Collection, ShopModel, UserModel
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
        print(request.data['cashierId'])

        

        serializer = CollectionSerializer(data=request.data)
        if serializer.is_valid():
            # serializer.save()
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











@api_view(['POST'])
def CollectionsAddView(request):
    if request.method == 'POST':
        # Check if 'cashierId' exists in the request data
        cashier_id = request.data.get('cashierId')
        # data = UserModel.objects.get(Q(user_id=cashier_id) & Q(user_role__user_role_name="Account"))

        data = UserModel.objects.filter(user_role__user_role_name="Account")
        print(data)

        # a=UserModel.objects.get(user_role=data.user_role_id)
        # print(a)

#         if cashier_id is not None:
#             # Assuming user_role is fetched from the user authentication or request context
#             # user_role = "account"  # Replace this with your logic to get the user_role

            

# # Assuming cashier_id and user_role_name are available



#             # Check if user_role is 'account'
#             if user_role == "account":
#                 # Proceed with adding data as user_role is 'account'
#                 serializer = CollectionSerializer(data=request.data)
#                 if serializer.is_valid():
#                     # serializer.save()
#                     response_data = {
#                         "message_text": "Success",
#                         "message_code": 1000,
#                         "message_data": serializer.data
#                     }
#                     return Response(response_data, status=status.HTTP_201_CREATED)

        return Response({
            "message_text": "Failure",
            "message_code": 999,
            "message_data": [],
        }, status=status.HTTP_400_BAD_REQUEST)