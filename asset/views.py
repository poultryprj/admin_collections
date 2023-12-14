from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Assets 

##################################### Assets Add ###################################################
################# Assets Add
def AssetAdd(request):
    if request.method == "POST":
        assetName = request.POST.get('asset_name')
        assetTypes = request.POST.get('asset_types')
        slowlyFinishedProduct = request.POST.get('slowly_finished_product')
        longLastingProducts = request.POST.get('long_lasting_products')

        # Determine which product field to populate based on the asset type selected
        if assetTypes == 'Slowly_Finished_Product':
            selectedProduct = slowlyFinishedProduct
        else:
            selectedProduct = longLastingProducts

        # Save the asset detail based on the selected product
        AssetsDetailAdd = Assets(
            asset_name=assetName,
            asset_types=assetTypes,
            created_by=request.user,
        )

        if assetTypes == 'Slowly_Finished_Product':
            AssetsDetailAdd.slowly_finished_product = selectedProduct
        else:
            AssetsDetailAdd.long_lasting_products = selectedProduct
        
        print(AssetsDetailAdd.asset_name,
              AssetsDetailAdd.asset_types,
              AssetsDetailAdd.slowly_finished_product,
              AssetsDetailAdd.long_lasting_products,
              AssetsDetailAdd.created_by)
        AssetsDetailAdd.save()

        messages.success(request, "Asset Detail Added Successfully..!!")
        return redirect('asset_add')  # Redirect to a success page or the same page

    assetTypes = ['Slowly_Finished_Product', 'Long_Lasting_Products']
    slowly_finished_product_types = ['Polyethylene_Bags', 'Paper_Bags']
    long_lasting_products_types = ['T-Shirt', 'Eggs_Tray', 'Dustbin']
    context = {
        'slowly_finished_product_types': slowly_finished_product_types,
        'long_lasting_products_types': long_lasting_products_types,
        'assetTypes': assetTypes
    }

    return render(request, 'asset/asset_add.html', context)


################# Asset List
def AssetList(request):
    AssetsList = Assets.objects.filter(is_deleted=False)

    context = {
        'AssetsList': AssetsList
    }
    return render(request, 'asset/asset_list.html', context)


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