import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from account import models
from shop.models import ProductMaster, ProductTypes
from user.models import UserModel
from vehicle1.models import ProductRecieve, Vehicle, VehicleMakeBy, VehicleModel, VehicleType, Vendor
from django.contrib import messages
from .models import Fitness, InsuranceCompany, ProductRecieve, VehicleInsurance, VehiclePermit, VehiclePollution, VehicleTax
from django.db import IntegrityError
from .models import Vehicle, InsuranceCompany, VehicleInsurance
from .models import InsuranceCompany, VehicleInsurance, Vehicle

############## Vehicle ######################################################################

def vehicle(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))  # Decode the JSON data
        addName = data.get('new_name')
        if addName:
            try:
                return JsonResponse({'success': True, 'new_name': addName})
    
            except Exception as e:
                return JsonResponse({'success': False, 'error_message': str(e)}, status=500)

############## Vehicle List            
def VehicleDetailList(request):

    vehicleDetailList = Vehicle.objects.all()
    print(vehicleDetailList)

    context = {
        'vehicleDetailList' : vehicleDetailList
    }
    return render(request, 'vehicle/vehicle_detail_list.html', context)



############## Vehicle Add
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

############## Vehicle Edit
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

############## Vehicle Update
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

############## Product Received List
def ProductReceivedList(request):
    print("ghhvhvhbv")
    productRecieveList = ProductRecieve.objects.filter(is_deleted = False)

    context ={
        'productRecieveList' : productRecieveList
    }

    return render(request, "received_products/received_product_list.html", context)

############## Product Received Add
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

############## Product Received Edit
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

############## Product Received Update
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

############## Product Received Delete
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
        

######################## Vehicle Fitness ##############################################################################
############## Vehicle Fitness Add
def VehicleFitnessAdd(request):
    vehicleData = Vehicle.objects.all()

    if request.method == "POST":
        vehicleId = request.POST['vehicle_id']
        vehicleFitnessFromDate = request.POST['vehicle_fitness_from_date']
        vehicleFitnessToDate = request.POST['vehicle_fitness_to_date']

        # Check if the vehicle ID exists
        existing_vehicle = Vehicle.objects.filter(vehicle_id=vehicleId).first()

        if existing_vehicle:
            try:
                # Check if fitness details already exist for this vehicle
                existing_fitness = Fitness.objects.filter(vehicle_id=existing_vehicle).exists()
                if existing_fitness:
                    messages.error(request, "Fitness details already exist for this vehicle.")
                else:
                    vehicleFitnessDetaildAdd = Fitness(
                        vehicle_id=existing_vehicle,
                        vehicle_fitness_from_date=vehicleFitnessFromDate,
                        vehicle_fitness_to_date=vehicleFitnessToDate,
                        created_by_id=request.user,
                        last_modified_by_id=request.user
                    )
                    vehicleFitnessDetaildAdd.save()
                    messages.success(request, "Vehicle Fitness Details Added...")
                    return redirect('vehicle_fitness_list')
            except IntegrityError as e:
                messages.error(request, str(e))
        else:
            # If vehicle ID does not exist, create a new one
            try:
                new_vehicle = Vehicle.objects.create(vehicle_id=vehicleId)
                vehicleFitnessDetaildAdd = Fitness(
                    vehicle_id=new_vehicle,
                    vehicle_fitness_from_date=vehicleFitnessFromDate,
                    vehicle_fitness_to_date=vehicleFitnessToDate,
                    created_by_id=request.user,
                    last_modified_by_id=request.user
                )
                vehicleFitnessDetaildAdd.save()
                messages.success(request, "Vehicle Fitness Details Added...")
                return redirect('vehicle_fitness_list')
            except IntegrityError as e:
                messages.error(request, str(e))

    context = {
        'vehicleData': vehicleData
    }

    return render(request, 'vehicle/vehicle_fitness_add.html', context)

############## Vehicle Fitness View List
def VehicleFitnessList(request):
    # Filter out deleted fitness details
    fitnessDetailList = Fitness.objects.filter(is_deleted=False)

    context = {
        'fitnessDetailList': fitnessDetailList
    }
    return render(request, 'vehicle/vehicle_fitness_list.html', context)


############## Vehicle Fitness Edit
def VehicleFitnessEdit(request, id):
    try:
        vehicleFitnessData = get_object_or_404(Fitness, fitness_id=id)
        vehicleDetailEdit = vehicleFitnessData.vehicle_id  

        context = {
            "vehicleDetailEdit": vehicleDetailEdit,
            'vehicleFitnessData': vehicleFitnessData,
        }
        return render(request, "vehicle/vehicle_fitness_edit.html", context)
    except Fitness.DoesNotExist:
        messages.error(request, "Fitness record not found.")
        return redirect('error_page')     

############## Vehicle Fitness Update
def VehicleFitnessDetailsUpdate(request):
    if request.method == "POST":
        fitness_id = request.POST['fitness_id']
        vehicleFitnessFromDate = request.POST['vehicle_fitness_from_date']
        vehicleFitnessToDate = request.POST['vehicle_fitness_to_date']

        # Assuming the Fitness model has a field called 'fitness_id'
        vehicleFitnessDetailsUpdate = get_object_or_404(Fitness, fitness_id=fitness_id)

        # vehicleFitnessDetailsUpdate.registration_no = registrationNo
        vehicleFitnessDetailsUpdate.vehicle_fitness_from_date = vehicleFitnessFromDate
        vehicleFitnessDetailsUpdate.vehicle_fitness_to_date = vehicleFitnessToDate
       
        vehicleFitnessDetailsUpdate.last_modified_by_id = request.user

        vehicleFitnessDetailsUpdate.save()

        messages.success(request, "Vehicle Fitness Details Updated Successfully..!!")
        return redirect('vehicle_fitness_list')



############## Vehicle Fitness Delete
def VehicleFitnessDetailsdelete(request, id):
    fitnessDetailData = get_object_or_404(Fitness, fitness_id=id)
    fitnessDetailData.is_deleted = True
    fitnessDetailData.deleted_by = request.user
    fitnessDetailData.save()
    fitnessDetailList = Fitness.objects.filter(is_deleted=False)  # Filter non-deleted items
    messages.success(request, "Vehicle Fitness Details Deleted Successfully..!!")
    return render(request, 'vehicle/vehicle_fitness_list.html', {'fitnessDetailList': fitnessDetailList})


###########################################################################################################################################################################
######## Show Vehicle All Details in single form
def ShowVehicleDetail(request, id):
    try:
        vehicleDetailEdit = Vehicle.objects.get(vehicle_id=id)
        vehicleMakeByData = VehicleMakeBy.objects.all()
        vehicleModelyData = VehicleModel.objects.all()
        vehicleTypeData = VehicleType.objects.all()
        
        fitnessDetailList = Fitness.objects.filter(is_deleted=False)
        vehicleFitnessData = fitnessDetailList.filter(vehicle_id=vehicleDetailEdit).first()
        
        context = {
            "vehicleDetailEdit": vehicleDetailEdit,
            'vehicleMakeByData': vehicleMakeByData,
            'vehicleModelyData': vehicleModelyData,
            'vehicleTypeData': vehicleTypeData,
            'vehicleFitnessData': vehicleFitnessData,
        }

        return render(request, 'vehicle/show_vehicle_details.html', context)
    
    except Vehicle.DoesNotExist:
        messages.error(request, "Vehicle record not found.")
        return redirect('error_page')
    except Fitness.DoesNotExist:
        vehicleFitnessData = None
        context = {
            "vehicleDetailEdit": vehicleDetailEdit,
            'vehicleMakeByData': vehicleMakeByData,
            'vehicleModelyData': vehicleModelyData,
            'vehicleTypeData': vehicleTypeData,
            'vehicleFitnessData': vehicleFitnessData,
        }
        return render(request, 'vehicle/show_vehicle_details.html', context)



#########Vehicle Insurance#################################################################################################################
########### Vehicle Insurance Add
def VehicleInsuranceAdd(request):
    vehicleData = Vehicle.objects.all()
    InsuranceCompanyData = InsuranceCompany.objects.all()

    if request.method == "POST":
        vehiclenewId = request.POST['vehicle_id']
        insuranceCompanyName = request.POST.get('insurance_company_name')  # Use get() instead of indexing directly
        insuranceFromDate = request.POST['insurance_from_date']
        insuranceToDate = request.POST['insurance_to_date']
        insuranceAmount = request.POST['insurance_amount']
        insurancePaidAmount = request.POST['insurance_paid_amount']

        vehicleId = get_object_or_404(Vehicle, vehicle_id=vehiclenewId)

        try:
            # Get or create an instance of InsuranceCompany
            insuranceCompany, created = InsuranceCompany.objects.get_or_create(
                insurance_company_name=insuranceCompanyName
            )

            vehicleInsuranceDetailAdd = VehicleInsurance(
                vehicle_id=vehicleId,
                insurance_company=insuranceCompany,
                insurance_from_date=insuranceFromDate,
                insurance_to_date=insuranceToDate,
                insurance_amount=insuranceAmount,
                insurance_paid_amount=insurancePaidAmount,
                created_by_id=request.user,
                last_modified_by_id=request.user,
            )

            # Save the new vehicle insurance detail to the database
            vehicleInsuranceDetailAdd.save()

            messages.success(request, "Vehicle Insurance Detail Added.")
            return redirect('vehicle_insurance_list')  # Redirect to a success page or the same page

        except IntegrityError as e:
            messages.error(request, str(e))

    context = {
        'vehicleData': vehicleData,
        'insuranceCompanies': InsuranceCompanyData,
    }

    return render(request, 'vehicle/vehicle_insurance_add.html', context)


############# Vehicle Insurance drop-down add
def VehicleInsuranceCompanyAdd(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        addName = data.get('new_name')
        
        if addName:
            try:
                new_company = InsuranceCompany.objects.create(insurance_company_name=addName)
                return JsonResponse({'success': True, 'new_name': new_company.insurance_company_name})
            
            except Exception as e:
                return JsonResponse({'success': False, 'error_message': str(e)}, status=500)
        
    return JsonResponse({'success': False})

########### Vehicle Insurance drop-down list
def VehicleInsuranceCompanyAddList(request):
    vehicleInsuranceDetailList = Vehicle.objects.all()
    context = {
        'vehicleInsuranceDetailList': vehicleInsuranceDetailList
    }
    return render(request, 'vehicle/vehicle_insurance_add.html', context)


########### Vehicle Insurance List View
def VehicleInsuranceList(request):
    vehicleInsuranceList = VehicleInsurance.objects.filter(is_deleted=False)

    context = {
        'vehicleInsuranceList': vehicleInsuranceList
    }
    return render(request, 'vehicle/vehicle_insurance_list.html', context)

########### Vehicle Insurance Edit
def VehicleInsuranceEdit(request, id):
    try:
        vehicleInsuranceData = get_object_or_404(VehicleInsurance, insurance_id=id)
        vehicleDetailEdit = vehicleInsuranceData.vehicle_id
        insuranceCompanyData = InsuranceCompany.objects.all()

        context = {
            'vehicleDetailEdit': vehicleDetailEdit,
            'vehicleInsuranceData': vehicleInsuranceData,
            'insuranceCompanyData': insuranceCompanyData  # Make sure this variable is passed to the context
        }
        return render(request, "vehicle/vehicle_insurance_edit.html", context)
    except VehicleInsurance.DoesNotExist:
        messages.error(request, "Vehicle Insurance record not found.")
        return redirect('error_page')
    

########### Vehicle Insurance Update
def vehicleInsuranceUpdate(request):
    if request.method == "POST":
        insurance_id = request.POST.get('insurance_id')

        vehicle_insurance = get_object_or_404(VehicleInsurance, insurance_id=insurance_id)
        insurance_company_name = request.POST.get('insurance_company_name')
        insurance_company = get_object_or_404(InsuranceCompany, insurance_company_name=insurance_company_name)

        vehicle_insurance.insurance_company = insurance_company
        vehicle_insurance.insurance_from_date = request.POST.get('insurance_from_date')
        vehicle_insurance.insurance_to_date = request.POST.get('insurance_to_date')
        vehicle_insurance.insurance_amount = request.POST.get('insurance_amount')
        vehicle_insurance.insurance_paid_amount = request.POST.get('insurance_paid_amount')
        vehicle_insurance.last_modified_by_id = request.user

        vehicle_insurance.save()

        messages.success(request, "Vehicle Insurance Details Updated Successfully..!!")
        return redirect('vehicle_insurance_list')
    
    return render(request, 'vehicle/vehicle_insurance_list.html',)

########### Vehicle Insurance Delete
def vehicleInsuranceDelete(request, id):
    vehicleInsuranceData = get_object_or_404(VehicleInsurance, insurance_id=id)
    vehicleInsuranceData.is_deleted = True
    vehicleInsuranceData.deleted_by = request.user
    vehicleInsuranceData.save()
    vehicleInsuranceList = VehicleInsurance.objects.filter(is_deleted=False)  # Filter non-deleted items
    messages.success(request, "Vehicle Insurance Details Deleted Successfully..!!")
    return render(request, 'vehicle/vehicle_insurance_list.html', {'vehicleInsuranceList': vehicleInsuranceList})


################# Vehicle Permit #########################################################################################################
################# Vehicle Permit ADD
def VehiclePermitAdd(request):
    vehicleData = Vehicle.objects.all()

    if request.method == "POST":
        vehiclenewId = request.POST['vehicle_id']
        vehiclePermitFromDate = request.POST['permit_from_date']
        vehiclePermitToDate = request.POST['permit_to_date']
        vehiclePermitType = request.POST['permit_type']
        vehiclePermitId = request.POST['vehicle_permit_id_no']

        vehicleId = get_object_or_404(Vehicle, vehicle_id=vehiclenewId)

        try:

            vehicleInsuranceDetailAdd = VehiclePermit(
                vehicle_id=vehicleId,
                vehicle_permit_from_Date=vehiclePermitFromDate,
                vehicle_permit_to_Date=vehiclePermitToDate,
                vehicle_permit_type=vehiclePermitType,
                vehicle_permit_id=vehiclePermitId,
                created_by_id=request.user,
                last_modified_by_id=request.user,
            )
            
            vehicleInsuranceDetailAdd.save()

            messages.success(request, "Vehicle Permit Detail Added.")
            return redirect('vehicle_permit_list')  # Redirect to a success page or the same page

        except IntegrityError as e:
            messages.error(request, str(e))

    TypeOfPermit = ['Private', 'Transport']
    context = {
        'vehicleData': vehicleData,
        'TypeOfPermit': TypeOfPermit,
    }

    return render(request, 'vehicle/vehicle_permit_add.html', context)

################# Vehicle Permit ADD
def VehiclePermitList(request):
    vehiclePermitList = VehiclePermit.objects.filter(is_deleted=False)

    context = {
        'vehiclePermitList': vehiclePermitList
    }
    return render(request, 'vehicle/vehicle_permit_list.html', context)

################# Vehicle permit edit
def VehiclePermitEdit(request, id):
    try:
        vehiclePermitData = get_object_or_404(VehiclePermit, permit_id=id)
        vehicleDetailEdit = vehiclePermitData.vehicle_id

        TypeOfPermit = ['Private', 'Transport']
        context = {
            'vehicleDetailEdit': vehicleDetailEdit,
            'vehiclePermitData': vehiclePermitData,
            'TypeOfPermit': TypeOfPermit,  # Make sure this variable is passed to the context
        }
        return render(request, "vehicle/vehicle_permit_edit.html", context)
    except VehicleInsurance.DoesNotExist:
        messages.error(request, "Vehicle Insurance record not found.")
        return redirect('error_page')
    
################# Vehicle permit update
def vehiclePermitUpdate(request):
    if request.method == "POST":
        permitId = request.POST.get('permit_id')

        vehiclePermitData = get_object_or_404(VehiclePermit, permit_id=permitId)

        vehiclePermitData.vehicle_permit_from_Date = request.POST.get('vehicle_permit_from_Date')
        vehiclePermitData.vehicle_permit_to_Date = request.POST.get('vehicle_permit_to_Date')
        vehiclePermitData.vehicle_permit_type = request.POST.get('permit_type')
        vehiclePermitData.vehicle_permit_id = request.POST.get('vehicle_permit_id')
        vehiclePermitData.last_modified_by_id = request.user

        vehiclePermitData.save()

        messages.success(request, "Vehicle Permit Details Updated Successfully..!!")
        return redirect('vehicle_permit_list')
    
    return render(request, 'vehicle/vehicle_permit_list.html',)

################# Vehicle permit delete
def vehiclePermitdelete(request, id):
    vehiclePermitData = get_object_or_404(VehiclePermit, permit_id=id)
    vehiclePermitData.is_deleted = True
    vehiclePermitData.deleted_by = request.user
    vehiclePermitData.save()
    vehiclePermitList = VehiclePermit.objects.filter(is_deleted=False)  # Filter non-deleted items
    messages.success(request, "Vehicle Permit Details Deleted Successfully..!!")
    return render(request, 'vehicle/vehicle_permit_list.html', {'vehiclePermitList': vehiclePermitList})

###############################################################################################################
################# Vehicle Pollution ADD
def VehiclePollutionAdd(request):
    vehicleData = Vehicle.objects.all()

    if request.method == "POST":
        vehiclenewId = request.POST['vehicle_id']
        vehiclePollutionFromDate = request.POST['vehicle_pollution_from_Date']
        vehiclePollutionToDate = request.POST['vehicle_pollution_to_Date']
        vehiclePollutionValue = request.POST['vehicle_pollution_value']

        vehicleId = get_object_or_404(Vehicle, vehicle_id=vehiclenewId)

        try:

            vehiclePollutionDetailAdd = VehiclePollution(
                vehicle_id=vehicleId,
                vehicle_pollution_from_Date=vehiclePollutionFromDate,
                vehicle_pollution_to_Date=vehiclePollutionToDate,
                vehicle_pollution_value=vehiclePollutionValue,
                created_by_id=request.user,
                last_modified_by_id=request.user,
            )

            vehiclePollutionDetailAdd.save()

            messages.success(request, "Vehicle Pollution Detail Added.")
            return redirect('vehicle_pollution_list')  # Redirect to a success page or the same page

        except IntegrityError as e:
            messages.error(request, str(e))

    context = {
        'vehicleData': vehicleData,
    }

    return render(request, 'vehicle/vehicle_pollution_add.html', context)

################# Vehicle Pollution list
def VehiclePollutionList(request):
    vehiclePollutionList = VehiclePollution.objects.filter(is_deleted=False)

    context = {
        'vehiclePollutionList': vehiclePollutionList
    }
    return render(request, 'vehicle/vehicle_pollution_list.html', context)

################# Vehicle Pollution edit
def VehiclePollutionEdit(request, id):
    try:
        vehiclePollutionData = get_object_or_404(VehiclePollution, pollution_id=id)
        vehicleDetailEdit = vehiclePollutionData.vehicle_id

        context = {
            'vehicleDetailEdit': vehicleDetailEdit,
            'vehiclePollutionData': vehiclePollutionData,
        }
        return render(request, "vehicle/vehicle_pollution_edit.html", context)
    except VehiclePollution.DoesNotExist:
        messages.error(request, "Vehicle Pollution record not found.")
        return redirect('error_page')
    
################# Vehicle Pollution update
def vehiclePollutionUpdate(request):
    if request.method == "POST":
        pollutionId = request.POST.get('pollution_id')

        vehiclePollutionData = get_object_or_404(VehiclePollution, pollution_id=pollutionId)

        vehiclePollutionData.vehicle_pollution_from_Date = request.POST.get('vehicle_pollution_from_Date')
        vehiclePollutionData.vehicle_pollution_to_Date = request.POST.get('vehicle_pollution_to_Date')
        vehiclePollutionData.vehicle_pollution_value = request.POST.get('vehicle_pollution_value')
        vehiclePollutionData.last_modified_by_id = request.user

        vehiclePollutionData.save()

        messages.success(request, "Vehicle Pollution Details Updated Successfully..!!")
        return redirect('vehicle_pollution_list')
    
    return render(request, 'vehicle/vehicle_pollution_list.html',)

################# Vehicle Pollution delete

def vehiclePollutiondelete(request, id):
    vehiclePollutionData = get_object_or_404(VehiclePollution, pollution_id=id)
    vehiclePollutionData.is_deleted = True
    vehiclePollutionData.deleted_by = request.user
    vehiclePollutionData.save()
    vehiclePollutionList = VehiclePollution.objects.filter(is_deleted=False)  # Filter non-deleted items
    messages.success(request, "Vehicle Pollution Details Deleted Successfully..!!")
    return render(request, 'vehicle/vehicle_pollution_list.html', {'vehiclePollutionList': vehiclePollutionList})


##################################### Vehicle Tax ###################################################
################# Vehicle Tax Add
def VehicleTaxAdd(request):
    vehicleData = Vehicle.objects.all()

    if request.method == "POST":
        vehiclenewId = request.POST['vehicle_id']
        vehicleTaxFromDate = request.POST['vehicle_tax_from_Date']
        vehicleTaxToDate = request.POST['vehicle_tax_to_Date']
        vehicleTaxType = request.POST['vehicle_tax_type']
        vehicleEnvironmentTax = request.POST['vehicle_environment_tax']
        vehicleProfessionalTax = request.POST['vehicle_professional_tax']

        vehicleId = get_object_or_404(Vehicle, vehicle_id=vehiclenewId)

        try:

            vehicleTaxDetailAdd = VehicleTax(
                vehicle_id=vehicleId,
                vehicle_tax_from_Date=vehicleTaxFromDate,
                vehicle_tax_to_Date=vehicleTaxToDate,
                vehicle_tax_type=vehicleTaxType,
                vehicle_environment_tax=vehicleEnvironmentTax,
                vehicle_professional_tax=vehicleProfessionalTax,

                created_by_id=request.user,
                last_modified_by_id=request.user,
            )

            vehicleTaxDetailAdd.save()

            messages.success(request, "Vehicle Tax Detail Added.")
            return redirect('vehicle_tax_list')  # Redirect to a success page or the same page

        except IntegrityError as e:
            messages.error(request, str(e))
    vehicleTaxTypes = ['Private', 'Transport']
    context = {
        'vehicleData': vehicleData,
        'vehicleTaxTypes' : vehicleTaxTypes,
    }

    return render(request, 'vehicle/vehicle_tax_add.html', context)


################# Vehicle Tax List
def VehicleTaxList(request):
    vehicleTaxList = VehicleTax.objects.filter(is_deleted=False)

    context = {
        'vehicleTaxList': vehicleTaxList
    }
    return render(request, 'vehicle/vehicle_tax_list.html', context)


################# Vehicle Tax Edit
def VehicleTaxEdit(request, id):
    try:
        vehicleTaxData = get_object_or_404(VehicleTax, tax_id=id)
        vehicleDetailEdit = vehicleTaxData.vehicle_id

        vehicleTaxTypes = ['Private', 'Transport']        
        context = {
            'vehicleDetailEdit': vehicleDetailEdit,
            'vehicleTaxData': vehicleTaxData,
            'vehicleTaxTypes': vehicleTaxTypes,
        }
        return render(request, "vehicle/vehicle_tax_edit.html", context)
    except VehicleTax.DoesNotExist:
        messages.error(request, "Vehicle Tax record not found.")
        return redirect('error_page')
    
    
################# Vehicle Tax Update
def vehicleTaxUpdate(request):
    if request.method == "POST":
        taxId = request.POST.get('tax_id')

        vehicleTaxData = get_object_or_404(VehicleTax, tax_id=taxId)

        vehicleTaxData.vehicle_tax_from_Date = request.POST.get('vehicle_tax_from_Date')
        vehicleTaxData.vehicle_tax_to_Date = request.POST.get('vehicle_tax_to_Date')
        vehicleTaxData.vehicle_tax_type = request.POST.get('vehicle_tax_type')
        vehicleTaxData.vehicle_environment_tax = request.POST.get('vehicle_environment_tax')
        vehicleTaxData.vehicle_professional_tax = request.POST.get('vehicle_professional_tax')
        vehicleTaxData.last_modified_by_id = request.user

        vehicleTaxData.save()

        messages.success(request, "Vehicle Tax Details Updated Successfully..!!")
        return redirect('vehicle_tax_list')
    
    return render(request, 'vehicle/vehicle_tax_list.html',)

################# Vehicle Tax delete
def vehicleTaxdelete(request, id):
    vehicleTaxData = get_object_or_404(VehicleTax, tax_id=id)
    vehicleTaxData.is_deleted = True
    vehicleTaxData.deleted_by = request.user
    vehicleTaxData.save()
    vehicleTaxList = VehicleTax.objects.filter(is_deleted=False)  # Filter non-deleted items
    messages.success(request, "Vehicle Tax Details Deleted Successfully..!!")
    return render(request, 'vehicle/vehicle_tax_list.html', {'vehicleTaxList': vehicleTaxList})