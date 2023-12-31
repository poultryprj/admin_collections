import datetime
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.shortcuts import render, redirect
from user.models import UserRole
from vehicle.models import Vendor
from .models import AssetPurchase, AssetStock, Assets, Vendor, AssetDistribution
from datetime import datetime
from django.contrib.auth.models import Group
from django.utils import timezone

##################################### Assets Add ###################################################
################# Assets Add #################
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
        return redirect('asset_list')  # Redirect to a success page or the same page

    assetTypes = ['Slowly_Finished_Product', 'Long_Lasting_Products']
    slowly_finished_product_types = ['Polyethylene_Bags', 'Paper_Bags']
    long_lasting_products_types = ['T-Shirt', 'Eggs_Tray', 'Dustbin']
    context = {
        'slowly_finished_product_types': slowly_finished_product_types,
        'long_lasting_products_types': long_lasting_products_types,
        'assetTypes': assetTypes
    }

    return render(request, 'asset/asset_add.html', context)


################# Asset List #################
def AssetList(request):
    AssetsList = Assets.objects.filter(is_deleted=False).order_by('-asset_id')

    context = {
        'AssetsList': AssetsList
    }
    return render(request, 'asset/asset_list.html', context)


################# Asset Edit #################
def AssetEdit(request, id):
    try:
        assetData = get_object_or_404(Assets, asset_id=id)

        assetTypes = ['Slowly_Finished_Product', 'Long_Lasting_Products']
        slowly_finished_product_types = ['Polyethylene_Bags', 'Paper_Bags']
        long_lasting_products_types = ['T-Shirt', 'Eggs_Tray', 'Dustbin']
        context = {
            'slowly_finished_product_types': slowly_finished_product_types,
            'long_lasting_products_types': long_lasting_products_types,
            'assetTypes': assetTypes,
            'assetData' : assetData
        }
        return render(request, "asset/asset_edit.html", context)
    except Exception as e:
        print(e)
    
    
################# Asset Update #################
def AssetUpdate(request):
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
            last_modified_by=request.user,
        )

        if assetTypes == 'Slowly_Finished_Product':
            AssetsDetailAdd.slowly_finished_product = selectedProduct
        else:
            AssetsDetailAdd.long_lasting_products = selectedProduct
        
        AssetsDetailAdd.save()

        messages.success(request, "Asset Detail Updated Successfully..!!")
        return redirect('asset_list')  # Redirect to a success page or the same page

    assetTypes = ['Slowly_Finished_Product', 'Long_Lasting_Products']
    slowly_finished_product_types = ['Polyethylene_Bags', 'Paper_Bags']
    long_lasting_products_types = ['T-Shirt', 'Eggs_Tray', 'Dustbin']
    context = {
        'slowly_finished_product_types': slowly_finished_product_types,
        'long_lasting_products_types': long_lasting_products_types,
        'assetTypes': assetTypes
    }

    return render(request, 'asset/asset_list.html', context)


################# Asset delete #################
def AssetDelete(request, id):
    assetData = get_object_or_404(Assets, asset_id=id)
    assetData.is_deleted = True
    assetData.deleted_by = request.user
    assetData.save()
    assetList = Assets.objects.filter(is_deleted=False)  # Filter non-deleted items
    messages.success(request, "Asset Details Deleted Successfully..!!")
    return render(request, 'asset/asset_list.html', {'AssetsList': assetList})



##################################### AssetPurchase ###################################################
################# AssetPurchase ###################
def AssetPurchaseAdd(request):
    assetData = Assets.objects.all()
    vendorData = Vendor.objects.all()

    if request.method == "POST":
        assetNewid = request.POST.get('asset_id')
        vendorNewid = request.POST.get('vendor_id') 
        purchase_date = request.POST.get('purchase_date')
        purchase_time = request.POST.get('purchase_time')
        purchase_on = datetime.strptime(f"{purchase_date} {purchase_time}", "%Y-%m-%d %H:%M")
        quantity = request.POST.get('quantity')
        weight = request.POST.get('weight')
        rate = request.POST.get('rate')
        amount = request.POST.get('amount')
        remarks = request.POST.get('remarks')

        assetId = get_object_or_404(Assets, asset_id=assetNewid)
        vendorId = get_object_or_404(Vendor, vendor_id=vendorNewid)

        # Create the AssetPurchase object
        asset_purchase_add = AssetPurchase(
            purchase_on=purchase_on,
            vendor_Id=vendorId,
            asset_Id=assetId,
            quantity=quantity,
            weight=weight,
            rate=rate,
            amount=amount,
            remarks=remarks,
            created_by=request.user,
            last_modified_by=request.user,
        )

        asset_purchase_add.save()

        messages.success(request, "Asset Purchase Details Added Successfully..!!")
        return redirect('asset_purchase_list')

    context = {
        'assetData': assetData,
        'vendorData': vendorData
    }

    return render(request, 'asset/asset_purchase_add.html', context)


################# Asset List #################
def AssetPurchaseList(request):
    AssetPrchaseList = AssetPurchase.objects.filter(is_deleted=False).order_by('-asset_purchase_id')

    context = {
        'AssetPrchaseList': AssetPrchaseList,
    }
    return render(request, 'asset/asset_purchase_list.html', context)


################# Asset Edit #################
# views.py

def AssetPurchaseEdit(request, id):
    try:
        assetData = Assets.objects.all()
        vendorData = Vendor.objects.all()
        assetPurchaseData = get_object_or_404(AssetPurchase, asset_purchase_id=id)

        # Extracting date and time from the purchase_on timestamp
        purchase_date = assetPurchaseData.purchase_on.strftime('%Y-%m-%d')
        purchase_time = assetPurchaseData.purchase_on.strftime('%H:%M')

        context = {
            'assetPurchaseData': assetPurchaseData,
            'purchase_date': purchase_date,  # Sending pre-fetched date to the template
            'purchase_time': purchase_time,  # Sending pre-fetched time to the template
            'assetData': assetData,
            'vendorData': vendorData
        }
        return render(request, "asset/asset_purchase_edit.html", context)
    except Exception as e:
        print(e)

    
    
################# Asset Update #################
def AssetPurchaseUpdate(request):
    assetData = Assets.objects.all()
    vendorData = Vendor.objects.all()
    if request.method == "POST":
        assetNewid = request.POST.get('asset_id')
        vendorNewid = request.POST.get('vendor_id') 
        purchase_date = request.POST.get('purchase_date')
        purchase_time = request.POST.get('purchase_time')
        purchase_on = datetime.strptime(f"{purchase_date} {purchase_time}", "%Y-%m-%d %H:%M")
        quantity = request.POST.get('quantity')
        weight = request.POST.get('weight')
        rate = request.POST.get('rate')
        amount = request.POST.get('amount')
        remarks = request.POST.get('remarks')

        assetId = get_object_or_404(Assets, asset_id=assetNewid)
        vendorId = get_object_or_404(Vendor, vendor_id=vendorNewid)

        # Create the AssetPurchase object
        asset_purchase_add = AssetPurchase(
            purchase_on=purchase_on,
            vendor_Id=vendorId,
            asset_Id=assetId,
            quantity=quantity,
            weight=weight,
            rate=rate,
            amount=amount,
            remarks=remarks,
            created_by=request.user,
            last_modified_by=request.user,
        )
        
        asset_purchase_add.save()

        messages.success(request, "Asset Purchase Detail Updated Successfully..!!")
        return redirect('asset_purchase_list')  # Redirect to a success page or the same page


    context = {
        'assetData' : assetData,
        'vendorData' : vendorData,

    }

    return render(request, 'asset/asset_purchase_list.html', context)


################# Asset delete #################
def AssetPurchaseDelete(request, id):
    assetPurchaseData = get_object_or_404(AssetPurchase, asset_purchase_id=id)
    assetPurchaseData.is_deleted = True
    assetPurchaseData.deleted_by = request.user
    assetPurchaseData.save()
    messages.success(request, "Asset Purchase Details Deleted Successfully..!!")
    return redirect('asset_purchase_list')

################# AssetDistribution Add #################
def AssetDistributionAdd(request):
    groups = Group.objects.all()

    if request.method == "POST":
        distribution_date = request.POST.get('distribution_date')
        distribution_time = request.POST.get('distribution_time')
        distribution_date_time = datetime.strptime(f"{distribution_date} {distribution_time}", "%Y-%m-%d %H:%M")
        assets_consumer_type = request.POST.get('assets_consumer_type')
        group_id = request.POST.get('group_id')
        distribution_to_id = request.POST.get('distribution_to_id')
        quantity = request.POST.get('quantity')
        weight = request.POST.get('weight')
        remarks = request.POST.get('remarks')

        group = get_object_or_404(Group, id=group_id)
        
        # Create the AssetDistribution object
        asset_distribution_add = AssetDistribution(
            distribution_date_and_time=distribution_date_time,
            assets_consumer_type=assets_consumer_type,
            user_group = group,
            distribution_to_id=distribution_to_id,
            quantity=quantity,
            weight=weight,
            remarks=remarks,
            created_by=request.user,
            last_modified_by=request.user,
        )

        print(asset_distribution_add.distribution_date_and_time,
           asset_distribution_add.assets_consumer_type,
           asset_distribution_add.user_group,
           asset_distribution_add.distribution_to_id,
           asset_distribution_add.quantity,
           asset_distribution_add.weight,
           asset_distribution_add.remarks,
           asset_distribution_add.created_by,
           asset_distribution_add.last_modified_by)
        asset_distribution_add.save()

        messages.success(request, "Asset Distribution Details Added Successfully..!!")
        return redirect('asset_distribution_list')

    context = {
        'groups': groups,
    }

    return render(request, 'asset/asset_distribution_add.html', context)


################# AssetDistribution List #################
def AssetDistributionList(request):
    AssetDistributionList = AssetDistribution.objects.filter(is_deleted=False).order_by('-asset_distribution_id')

    context = {
        'AssetDistributionList': AssetDistributionList,
    }
    return render(request, 'asset/asset_distribution_list.html', context)



################# AssetDistribution Edit #################
def AssetDistributionEdit(request, id):
    groups = Group.objects.all()
    try:
        assetDistributionData = get_object_or_404(AssetDistribution, asset_distribution_id=id)

        # Extracting date and time from the distribution_date_and_time timestamp
        distribution_date = assetDistributionData.distribution_date_and_time.strftime('%Y-%m-%d')
        distribution_time = assetDistributionData.distribution_date_and_time.strftime('%H:%M')

        context = {
            'assetDistributionData': assetDistributionData,
            'distribution_date': distribution_date,  # Sending pre-fetched date to the template
            'distribution_time': distribution_time,  # Sending pre-fetched time to the template
            'groups': groups,
        }
        return render(request, "asset/asset_distribution_edit.html", context)
    except Exception as e:
        print(e)

################# AssetDistribution Update #################
def AssetDistributionUpdate(request):
    groups = Group.objects.all()
    if request.method == "POST":
        distribution_date = request.POST.get('distribution_date')
        distribution_time = request.POST.get('distribution_time')
        distribution_date_time = datetime.strptime(f"{distribution_date} {distribution_time}", "%Y-%m-%d %H:%M")
        consumer_type = request.POST.get('assets_consumer_type')
        group_id = request.POST.get('group_id')  # Assuming this field exists in your form
        distribution_to_id = request.POST.get('distribution_to_id')
        quantity = request.POST.get('quantity')
        weight = request.POST.get('weight')
        remarks = request.POST.get('remarks')

        user_group = get_object_or_404(Group, id=group_id)

        assetDistributionData = get_object_or_404(AssetDistribution, asset_distribution_id=request.POST.get('asset_distribution_id'))
        assetDistributionData.distribution_date_and_time = distribution_date_time
        assetDistributionData.assets_consumer_type = consumer_type if consumer_type else ''  # Assign a default value if consumer_type is None or empty

        # Update the AssetDistribution object
        assetDistributionData.distribution_date_and_time = distribution_date_time
        assetDistributionData.assets_consumer_type = consumer_type
        assetDistributionData.user_group = user_group  # Assigning the user group
        assetDistributionData.distribution_to_id = distribution_to_id
        assetDistributionData.quantity = quantity
        assetDistributionData.weight = weight
        assetDistributionData.remarks = remarks
        assetDistributionData.last_modified_by = request.user

        assetDistributionData.save()

        messages.success(request, "Asset Distribution Detail Updated Successfully..!!")
        return redirect('asset_distribution_list')

    context = {
        'groups': groups,
    }

    return render(request, 'asset/asset_distribution_list.html', context)



################# AssetDistribution Delete #################
def AssetDistributionDelete(request, id):
    assetDistributionData = get_object_or_404(AssetDistribution, asset_distribution_id=id)
    assetDistributionData.is_deleted = True
    assetDistributionData.deleted_by = request.user
    assetDistributionData.save()
    messages.success(request, "Asset Distribution Details Deleted Successfully..!!")
    return redirect('asset_distribution_list')



##################################### AssetStock ########################################
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import AssetStock
from datetime import datetime

def create_asset_stock(request):
    if request.method == 'POST':
        asset_id = request.POST.get('asset_id')
        quantity = request.POST.get('asset_stock_quantity')
        weight = request.POST.get('asset_stock_weight')
        created_by = request.user  # Assuming the logged-in user is creating this asset stock

        # Create AssetStock instance
        asset_stock = AssetStock.objects.create(
            asset_Id_id=asset_id,
            asset_stock_quantity=quantity,
            asset_stock_weight=weight,
            created_by=created_by
        )

        messages.success(request, "Asset Stock Details Added Successfully..!!")
        return redirect('asset_stock_detail', stock_id=asset_stock.stock_id)

    return render(request, 'create_asset_stock.html')

def asset_stock_detail(request, stock_id):
    asset_stock = get_object_or_404(AssetStock, stock_id=stock_id)
    return render(request, 'asset_stock_detail.html', {'asset_stock': asset_stock})

def update_asset_stock(request, stock_id):
    asset_stock = get_object_or_404(AssetStock, stock_id=stock_id)

    if request.method == 'POST':
        asset_stock.asset_stock_quantity = request.POST.get('asset_stock_quantity')
        asset_stock.asset_stock_weight = request.POST.get('asset_stock_weight')
        asset_stock.last_modified_by = request.user  # Assuming the logged-in user is updating this asset stock
        asset_stock.save()

        messages.success(request, "Asset Stock Detail Updated Successfully..!!")
        return redirect('asset_stock_detail', stock_id=asset_stock.stock_id)

    return render(request, 'update_asset_stock.html', {'asset_stock': asset_stock})

def delete_asset_stock(request, stock_id):
    asset_stock = get_object_or_404(AssetStock, stock_id=stock_id)

    if request.method == 'POST':
        asset_stock.is_deleted = True
        asset_stock.deleted_by = request.user  # Assuming the logged-in user is deleting this asset stock
        asset_stock.save()

        messages.success(request, "Asset Stock Details Deleted Successfully..!!")
        return redirect('asset_stock_list')

    return render(request, 'confirm_delete_asset_stock.html', {'asset_stock': asset_stock})
