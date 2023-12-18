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


################# Asset List
def AssetList(request):
    AssetsList = Assets.objects.filter(is_deleted=False)

    context = {
        'AssetsList': AssetsList
    }
    return render(request, 'asset/asset_list.html', context)


################# Asset Edit
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
    
    
################# Asset Update
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


################# Asset delete
def Assetdelete(request, id):
    assetData = get_object_or_404(Assets, asset_id=id)
    assetData.is_deleted = True
    assetData.deleted_by = request.user
    assetData.save()
    assetList = Assets.objects.filter(is_deleted=False)  # Filter non-deleted items
    messages.success(request, "Asset Details Deleted Successfully..!!")
    return render(request, 'asset/asset_list.html', {'AssetsList': assetList})