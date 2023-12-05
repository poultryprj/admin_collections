import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from shop.models import ProductMaster, ProductTypes
from user.models import UserModel
from vehicle_app.models import ProductRecieve, Vehicle, VehicleMakeBy, VehicleModel, VehicleType, Vendor
from django.contrib import messages

from django.shortcuts import get_object_or_404, redirect, render
from .models import ProductRecieve


def vehicle(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))  # Decode the JSON data
        addName = data.get('new_name')
        if addName:
            try:
                return JsonResponse({'success': True, 'new_name': addName})
    
            except Exception as e:
                return JsonResponse({'success': False, 'error_message': str(e)}, status=500)
            
def VehicleDetailList(request):

    vehicleDetailList = Vehicle.objects.all()
    print(vehicleDetailList)

    context = {
        'vehicleDetailList' : vehicleDetailList
    }
    return render(request, 'vehicle/vehicle_detail_list.html', context)



from django.db import IntegrityError
# ... (other imports and views)

from django.db import IntegrityError

def VehicleDetailAdd(request):
    vehicleMakeByData = VehicleMakeBy.objects.all()
    vehicleModelyData = VehicleModel.objects.all()
    vehicleTypeData = VehicleType.objects.all()

    if request.method == "POST":
        registrationNo = request.POST['registration_no']
        ownerName = request.POST['owner_name']
        vehicleMake = request.POST['vehicle_make_by']
        vehicleModel = request.POST['vehicle_model']
        vehicleType = request.POST['vehicle_type']
        vehicleDetails = request.POST['vehicle_details']
        fuelType = request.POST['fuel_type']
        wheelNo = request.POST['no_of_wheel']
        carrierType = request.POST['carrier_type']
        registrationDate = request.POST['registration_date']

        try:
            vehicleMakeId = VehicleMakeBy.objects.get(vehicle_make_by=vehicleMake)
        except VehicleMakeBy.DoesNotExist:
            vehicleMakeId = VehicleMakeBy.objects.create(vehicle_make_by=vehicleMake)

        try:
            vehicleModelId = VehicleModel.objects.get(vehicle_model=vehicleModel)
        except VehicleModel.DoesNotExist:
            vehicleModelId = VehicleModel.objects.create(vehicle_model=vehicleModel)

        try:
            vehicleTypeId = VehicleType.objects.get(vehicle_type=vehicleType)
        except VehicleType.DoesNotExist:
            vehicleTypeId = VehicleType.objects.create(vehicle_type=vehicleType)

        try:
            vehicleDetaildAdd = Vehicle(
                registration_no=registrationNo,
                owner_name=ownerName,
                vehicle_make_Id=vehicleMakeId,
                vehicle_model=vehicleModelId,
                vehicle_type=vehicleTypeId,
                vehicle_details=vehicleDetails,
                fuel_type=fuelType,
                no_of_wheel=wheelNo,
                carrier_type=carrierType,
                registration_date=registrationDate
            )
            vehicleDetaildAdd.save()

            messages.success(request, "Vehicle Detail Added.")
            return redirect('vehicle_detail_list')
        
        except IntegrityError as e:
            messages.error(request, str(e))

    context = {
        'vehicleMakeByData': vehicleMakeByData,
        'vehicleModelyData': vehicleModelyData,
        'vehicleTypeData': vehicleTypeData
    }
    return render(request, 'vehicle/vehicle_detail_add.html', context)


def VehicleDetailEdit(request, id):
    vehicleDetailEdit = Vehicle.objects.get(vehicle_id = id)
    vehicleMakeByData = VehicleMakeBy.objects.all()
    vehicleModelyData = VehicleModel.objects.all()
    vehicleTypeData = VehicleType.objects.all()

    context = {
        "vehicleDetailEdit":vehicleDetailEdit,
        'vehicleMakeByData' : vehicleMakeByData,
        'vehicleModelyData' : vehicleModelyData,
        'vehicleTypeData' : vehicleTypeData

    }
    return render(request, "vehicle/vehicle_detail_edit.html", context)


def VehicleDetailsUpdate(request):
    if request.method == "POST":
        vehicleDetailId = request.POST['vehicle_id']
        registrationNo = request.POST['registration_no']
        ownerName = request.POST['owner_name']
        vehicleMake = request.POST['vehicle_make_Id']
        vehicleModel = request.POST['vehicle_model_Id']
        vehicleType = request.POST['vehicle_type_Id']
        vehicleDetails = request.POST['vehicle_details']
        fuelType = request.POST['fuel_type']
        wheelNo = request.POST['no_of_wheel']
        carrierType = request.POST['carrier_type']
        registrationDate = request.POST['registration_date']


        vehicleMake = VehicleMakeBy.objects.get(vehicle_make_id = vehicleMake)
        vehicleModel = VehicleModel.objects.get(vehicle_model_id = vehicleModel)
        vehicleType = VehicleType.objects.get(vehicle_type_id = vehicleType)

        vehicleDetailUpdateData = Vehicle.objects.get(vehicle_id = vehicleDetailId)

        vehicleDetailUpdateData.registration_no = registrationNo
        vehicleDetailUpdateData.owner_name = ownerName
        vehicleDetailUpdateData.vehicle_make_Id = vehicleMake
        vehicleDetailUpdateData.vehicle_model = vehicleModel
        vehicleDetailUpdateData.vehicle_type = vehicleType

        vehicleDetailUpdateData.vehicle_details = vehicleDetails
        
        vehicleDetailUpdateData.fuel_type = fuelType
        
        vehicleDetailUpdateData.no_of_wheel = wheelNo
        
        vehicleDetailUpdateData.carrier_type = carrierType
        
        vehicleDetailUpdateData.registration_date = registrationDate

        vehicleDetailUpdateData.save()

        messages.success(request, "Vehicle Detail Updated.")
        return redirect('vehicle_detail_list')




### PRODUCT RECEIVED


def ProductReceivedList(request):
    print("ghhvhvhbv")
    productRecieveList = ProductRecieve.objects.filter(is_deleted = False)

    context ={
        'productRecieveList' : productRecieveList
    }

    return render(request, "received_products/received_product_list.html", context)


def ProductReceivedAdd(request):
    vendorData = Vendor.objects.all()
    productTypesData = ProductTypes.objects.all()
    productMasterData = ProductMaster.objects.all()
    vehicleData = Vehicle.objects.all()
    userModelData = UserModel.objects.all()


    if request.method == "POST":
        receiveDate = request.POST['received_date']
        vendorId = request.POST['vendor_id']
        productTypeId = request.POST['product_type_id']
        productId = request.POST['product_id']
        paperRate = request.POST['paper_rate']
        receivedQuantity = request.POST['received_quantity']
        receivedWeight = request.POST['received_weight']     
        receivedDailyRate = request.POST['received_daily_rate']
        receivedTcsRate = request.POST['received_tcs_rate']
        receivedTcsValue = request.POST['received_tcs_value']
        amount = request.POST['amount']
        receivedAmount = request.POST['received_amount']
        vehicleId = request.POST['vehicle_id']
        driverId = request.POST['driver_id']
        sourceVehicleId = request.POST['source_vehicle_id']
        sourceDriverId = request.POST['source_driver_id']
        challanNo = request.POST['challan_no']
        entrySource = request.POST['entry_source']
        latitude = request.POST['latitude']
        longitude = request.POST['longitude']
        
        print(receiveDate, vendorId, productTypeId, productId, paperRate, receivedQuantity, receivedWeight, receivedDailyRate, receivedTcsRate, 
              receivedTcsValue, amount , receivedAmount, vehicleId, driverId, sourceVehicleId, sourceDriverId, challanNo, entrySource, latitude, longitude)
        
        vendorId = Vendor.objects.get(vendor_id=vendorId)
        productTypesId = ProductTypes.objects.get(product_type_id=productTypeId)
        productMasterId = ProductMaster.objects.get(product_id=productId)
        vehicleId = Vehicle.objects.get(vehicle_id=vehicleId)
        userModelId = UserModel.objects.get(user_id=driverId)

        productRecieveDataAdd = ProductRecieve(
            recieved_date = receiveDate,
            vendorId = vendorId,
            product_typeId = productTypesId,
            productId = productMasterId,
            paper_rate = paperRate,
            recieved_quantity = receivedQuantity,
            recieved_weight = receivedWeight,
            daily_rate = receivedDailyRate,
            tcs_rate = receivedTcsRate,
            tcs_value = receivedTcsValue,
            amount = amount,
            recieved_amount = receivedAmount,
            vehicleId = vehicleId,
            driverId = userModelId,
            source_vehicle_id = sourceVehicleId,
            source_driver_id = sourceDriverId,
            challan_no = challanNo,
            entry_source = entrySource,
            latitude = latitude,
            longtitude = longitude,
            created_by = request.user,
            last_modified_by = request.user

        )
        productRecieveDataAdd.save()
        messages.success(request, "Product Received Add Successfully..!!")
        return redirect('product_received_list')

    
    context = {
        "vendorData" : vendorData,
        "productTypesData" : productTypesData,
        "productMasterData" : productMasterData,
        "vehicleData" : vehicleData,
        "userModelData" : userModelData

    }
        
    return render(request, "received_products/received_product_add.html", context)


def ProductReceivedEdit(request,id):
    productRecieveDataEdit = ProductRecieve.objects.get(product_record_id = id)


    vendorData = Vendor.objects.all()
    productTypesData = ProductTypes.objects.all()
    productMasterData = ProductMaster.objects.all()
    vehicleData = Vehicle.objects.all()
    userModelData = UserModel.objects.all()

    context = {
        'productRecieveDataEdit' : productRecieveDataEdit,
        "vendorData" : vendorData,
        "productTypesData" : productTypesData,
        "productMasterData" : productMasterData,
        "vehicleData" : vehicleData,
        "userModelData" : userModelData
    }
    return render(request, "received_products/received_product_edit.html", context) 


def ProductReceivedUpdate(request):
    if request.method == "POST":
        productReceivedId = request.POST['product_received_id']
        receiveDate = request.POST['received_date']
        vendorId = request.POST['vendor_id']
        productTypeId = request.POST['product_type_id']
        productId = request.POST['product_id']
        paperRate = request.POST['paper_rate']
        receivedQuantity = request.POST['received_quantity']
        receivedWeight = request.POST['received_weight']     
        receivedDailyRate = request.POST['received_daily_rate']
        receivedTcsRate = request.POST['received_tcs_rate']
        receivedTcsValue = request.POST['received_tcs_value']
        amount = request.POST['amount']
        receivedAmount = request.POST['received_amount']
        vehicleId = request.POST['vehicle_id']
        driverId = request.POST['driver_id']
        sourceVehicleId = request.POST['source_vehicle_id']
        sourceDriverId = request.POST['source_driver_id']
        challanNo = request.POST['challan_no']
        entrySource = request.POST['entry_source']
        latitude = request.POST['latitude']
        longitude = request.POST['longitude']



        vendorId = Vendor.objects.get(vendor_id=vendorId)
        productTypesId = ProductTypes.objects.get(product_type_id=productTypeId)
        productMasterId = ProductMaster.objects.get(product_id=productId)
        vehicleId = Vehicle.objects.get(vehicle_id=vehicleId)
        userModelId = UserModel.objects.get(user_id=driverId)

        productRecieveDataUpdate = ProductRecieve.objects.get(product_record_id = productReceivedId)
        productRecieveDataUpdate.recieved_date = receiveDate
        productRecieveDataUpdate.vendorId = vendorId
        productRecieveDataUpdate.product_typeId = productTypesId
        productRecieveDataUpdate.productId = productMasterId
        productRecieveDataUpdate.paper_rate = paperRate
        productRecieveDataUpdate.recieved_quantity = receivedQuantity
        productRecieveDataUpdate.recieved_weight = receivedWeight
        productRecieveDataUpdate.daily_rate = receivedDailyRate
        productRecieveDataUpdate.tcs_rate = receivedTcsRate
        productRecieveDataUpdate.tcs_value = receivedTcsValue
        productRecieveDataUpdate.amount = amount
        productRecieveDataUpdate.recieved_amount = receivedAmount
        productRecieveDataUpdate.vehicleId = vehicleId
        productRecieveDataUpdate.driverId = userModelId
        productRecieveDataUpdate.source_vehicle_id = sourceVehicleId
        productRecieveDataUpdate.source_driver_id = sourceDriverId
        productRecieveDataUpdate.challan_no = challanNo
        productRecieveDataUpdate.entry_source = entrySource
        productRecieveDataUpdate.latitude = latitude
        productRecieveDataUpdate.longtitude = longitude
        productRecieveDataUpdate.last_modified_by = request.user
        productRecieveDataUpdate.save()

        messages.success(request, "Product Received Updated Successfully..!!")
        return redirect('product_received_list')



from django.http import JsonResponse

def product_received_delete(request, id):
    if request.method == 'POST':
        print("HGJHGJHBVJHB")
        print(id)
        try:
            data = json.loads(request.body.decode('utf-8'))
            delete_reason = data.get('delete_reason')  # Assuming you're using POST method to send data
            print(delete_reason)

            productRecieveDataDelete = ProductRecieve.objects.get(product_record_id = id)
            productRecieveDataDelete.is_deleted = True
            productRecieveDataDelete.deleted_by = request.user
            productRecieveDataDelete.delete_reason  = delete_reason
            productRecieveDataDelete.save()

            # Perform necessary deletion logic
            
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)


# if request.method == "POST":
#         data = json.loads(request.body.decode('utf-8'))  # Decode the JSON data
#         addName = data.get('new_name')
#         if addName:
#             try:
#                 return JsonResponse({'success': True, 'new_name': addName})
    
#             except Exception as e:
#                 return JsonResponse({'success': False, 'error_message': str(e)}, status=500)