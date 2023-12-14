import json
from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from user.models import UserModel

from vehicle2.models import Vehicle, Vendor
from .models import  Associations, ProductRecieve, ShopBalance, ShopFlexibleRate, ShopModel, ShopOwner, ShopProductRates, ShopRoute, ProductTypes, ProductCategories, ProductMaster
from routes.models import RouteModel
from django.core.exceptions import ValidationError

# Create your views here.



def ShopList(request):

    shopLists = ShopModel.objects.filter(is_deleted=False)
 
    return render(request, 'shops/shop_list.html', context={'shopLists': shopLists})




def ShopBalanceDetails(request,id):
    shopBalance  = None
    shopModel = None
    try:
        shopBalance = ShopBalance.objects.get(shopId=id)
    except ShopBalance.DoesNotExist:
        shopModel = ShopModel.objects.get(shop_id=id)
        print(shopModel)
    context={
        'shopAndBalance' : shopBalance,
        'shopModel' : shopModel
    } 
    return render(request, 'shops/demo2.html', context)


def ShopAdd(request):

    shopOwnerData = ShopOwner.objects.all()

    if request.method == "POST":
        shopCode = request.POST['shop_code']
        shopName = request.POST['shop_name']
        shopArea = request.POST['shop_area']
        shopLatitude = request.POST['shop_latitude']
        shopLongitude = request.POST['shop_longitude']
        shopAddress = request.POST['shop_address']
        shopPinCode = request.POST['shop_pincode']
        shopDistance = request.POST['shop_distance']
        shopMobileNo = request.POST['shop_mobileNo']
        shopAlternateNo = request.POST['shop_alternateNo']
        shopOwnerId = request.POST['shop_ownerId']
        shoptype = request.POST['shop_type']
        shopStatus = request.POST['shop_status']

        shopAdd = ShopModel(
            shop_code = shopCode,
            shop_name = shopName,
            shop_area = shopArea,
            shop_latitude = shopLatitude,
            shop_longitude = shopLongitude,
            shop_address = shopAddress,
            shop_pincode = shopPinCode,
            shop_distance = shopDistance,
            shop_mobileNo = shopMobileNo,
            shop_alternateNo = shopAlternateNo,
            shop_type = shoptype,
            shop_status = shopStatus,
        )
        
        ownerId1 = ShopOwner.objects.get(owner_id=shopOwnerId)

        shopAdd.shop_ownerId = ownerId1
        shopAdd.save()

        messages.success(request, "Shop Name {} Add in the database.".format(shopName))
        return redirect('shop_list')
    
    return render(request, 'shops/shop_add.html', context={'shopOwnerData': shopOwnerData})



def ShopEdit(request, id):

    shopOwnerData = ShopOwner.objects.all()

    shopEdit  = ShopModel.objects.get(shop_id=id)

    return render(request, 'shops/shop_edit.html', context={'shopEdit' : shopEdit, 'shopOwnerData': shopOwnerData})



def ShopUpdate(request):
    if request.method == "POST":
        shopId = request.POST['shop_id']
        shopCode = request.POST['shop_code']
        shopName = request.POST['shop_name']
        shopArea = request.POST['shop_area']
        shopLatitude = request.POST['shop_latitude']
        shopLongitude = request.POST['shop_longitude']
        shopAddress = request.POST['shop_address']
        shopPinCode = request.POST['shop_pincode']
        shopDistance = request.POST['shop_distance']
        shopMobileNo = request.POST['shop_mobileNo']
        shopAlternateNo = request.POST['shop_alternateNo']
        shopOwnerId = request.POST['shop_ownerId']
        shoptype = request.POST['shop_type']
        shopStatus = request.POST['shop_status']

        shopUpdate = ShopModel.objects.get(shop_id=shopId)
        shopUpdate.shop_code = shopCode
        shopUpdate.shop_name = shopName
        shopUpdate.shop_area = shopArea
        shopUpdate.shop_latitude = shopLatitude
        shopUpdate.shop_longitude = shopLongitude
        shopUpdate.shop_address = shopAddress
        shopUpdate.shop_pincode = shopPinCode
        shopUpdate.shop_distance = shopDistance
        shopUpdate.shop_mobileNo = shopMobileNo
        shopUpdate.shop_alternateNo = shopAlternateNo
        # shopUpdate.shop_ownerId = shopOwnerId
        shopUpdate.shop_type = shoptype
        shopUpdate.shop_status = shopStatus
        
        ownerId1 = ShopOwner.objects.get(owner_id=shopOwnerId)

        shopUpdate.shop_ownerId = ownerId1
        shopUpdate.save()

        messages.success(request, "Shop Name:  {} Update in the database.".format(shopName))
        return redirect('shop_list')
    


def ShopDelete(request,id):
    shopDelete = ShopModel.objects.get(shop_id=id)
    shopDelete.is_deleted = True
    shopDelete.save()
    return redirect('shop_list')




# =================================================== Shop Owner ============================================================


def ShopOwnerList(request):

    shopOwnerLists = ShopOwner.objects.all()

    return render(request, 'shopOwners/shop_owners_list.html', context={'shopOwnerLists':shopOwnerLists})


def ShopOwnerAdd(request):
    if request.method == "POST":
        ownerName = request.POST['owner_name']
        ownerMob = request.POST['owner_mobileNo']
        ownerAltMob = request.POST['owner_alternateNo']

        shopOwnerAdd = ShopOwner(
            owner_name = ownerName ,
            owner_contactNo = ownerMob,
            owner_alternateNo = ownerAltMob,
            created_by = request.user,
            last_modified_by = request.user,
        )
        shopOwnerAdd.save()

        messages.success(request, "Shop Owner {} Add in the database.".format(ownerName))
        return redirect('shop_owner_list')

    return render(request, 'shopOwners/shop_owner_add.html')



def ShopOwnerEdit(request,id):

    shopOwnerEdit = ShopOwner.objects.get(owner_id=id)
    
    context={
        'shopOwnerEdit' : shopOwnerEdit
    }
    return render(request, 'shopOwners/shop_owner_edit.html',context)


def ShopOwnerUpdate(request):
    if request.method == "POST":
        ownerId = request.POST['owner_id']
        ownerName = request.POST['owner_name']
        ownerContact = request.POST['owner_contact']
        ownerAltContact = request.POST['owner_alt_contact']

        user = request.user.username
 
        ownerUpdate = ShopOwner.objects.get(owner_id=ownerId)

        ownerUpdate.owner_name = ownerName
        ownerUpdate.owner_contactNo = ownerContact
        ownerUpdate.owner_alternateNo = ownerAltContact
        ownerUpdate.last_modified_by = user
        ownerUpdate.save()

        messages.success(request, "Shop Owner:  {} Update in the database.".format(ownerName))
        return redirect('shop_owner_list')
    


def ShopOwnerDelete(request,id):
    shopOwnerDelete = ShopOwner.objects.get(owner_id=id)

    shopOwnerDelete.is_deleted = True
    shopOwnerDelete.deleted_by=request.user.username
    shopOwnerDelete.save()
    return redirect('shop_owner_list')


# *************************************** Shop Route **************************************

def ShopRouteList(request):
    routes = RouteModel.objects.all()
    shopsList = ShopModel.objects.all()
    selected_route = None
    selected_shop_ids = None
    shops = []
    shopCount = 0
    selected_shops = []

    if 'route_id' in request.GET:
        route_id = request.GET["route_id"]

        if route_id:
            selected_route = RouteModel.objects.get(route_id=route_id)
            shops = ShopRoute.objects.filter(route_id=selected_route)
            shopCount = shops.count()

    if 'selected_shops' in request.GET:
        selected_shop_ids = request.GET.getlist("selected_shops")
        selected_shops = ShopModel.objects.filter(pk__in=selected_shop_ids)

    context = {
        'routes': routes,
        'selected_route': selected_route,
        'shops': shops,
        'shopCount': shopCount,
        'shopsList': shopsList,
        'selected_shop_ids': selected_shop_ids,
        'selected_shops': selected_shops
    }

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse(context)

    return render(request, 'shop_routes/shop_route.html', context)





# def selected_shops(request):
#     if request.method == "POST":
#         selected_shop_ids = request.POST.getlist("selected_shops")
#         print(selected_shop_ids)
#         return render(request, 'shop_routes/shop_route.html',{'selected_shops': selected_shops})  

#     return render(request, 'shop_routes/shop_route.html')  



# *************************************** Product Type *************************************************

def ProductTypeList(request):

    productTypeList = ProductTypes.objects.all()

    context = {
        'productTypeList' : productTypeList
    }

    return render(request, 'product/product_type.html', context)




def ProductTypeAdd(request):
    if request.method == "POST":
        productTypeName = request.POST['product_type_name'].capitalize().strip()

        if not productTypeName:
            messages.error(request, "Product type name cannot be empty.")
        else:
            try:
                productTypeData, created = ProductTypes.objects.get_or_create(product_type=productTypeName)
                
                if created:
                    messages.success(request, "Product Type '{}' added to the database.".format(productTypeName))
                else:
                    messages.error(request, "Product Type '{}' already exists in the database.".format(productTypeName))
                
            except ValidationError:
                messages.error(request, "Invalid product type name.")

        return redirect('product_type')





def ProductTypeEdit(request,id):
    if request.method == "POST":
        productTypeName=request.POST['product_type_name'].capitalize().strip()

        productTypeId = ProductTypes.objects.get(product_type_id=id)
        productTypeId.product_type = productTypeName
        productTypeId.save()

        messages.success(request, "Product Type :  {} Update in the database.".format(productTypeName))
        return redirect('product_type')


# *************************************** Product Category *************************************************


def ProductCategoriesList(request):
    productCategories = ProductCategories.objects.all()

    context = {
        'productCategories' : productCategories
    }
    return render(request, 'product/product_categories.html', context)



def ProductCategoriesAdd(request):
    if request.method == "POST":
        categoryname = request.POST['product_category_name'].capitalize().strip()

        productCategoryData = ProductCategories(product_category = categoryname)
        productCategoryData.save()

        messages.success(request, "Product Category :  {} Add in the database.".format(categoryname))
        return redirect('product_categories')
    


def ProductTypeUpdate(request,id):
    if request.method == "POST":
        productCategoryName=request.POST['product_category_name'].capitalize().strip()

        productTypeId = ProductCategories.objects.get(product_category_id=id)
        productTypeId.product_category = productCategoryName
        productTypeId.save()

        messages.success(request, "Product Category :  {} Update in the database.".format(productCategoryName))
        return redirect('product_categories')
    



# *************************************** Product Master **************************

def ProductList(request):
     
    productData = ProductMaster.objects.filter(is_deleted = False)

    context = {
        'productData': productData,
    }

    return render(request, 'product/product_list.html', context) 




def ProductAdd(request):
    productTypeData = ProductTypes.objects.all()
    ProductCategoriesData = ProductCategories.objects.all()

    if request.method == "POST":
        productName = request.POST['product_name'].capitalize().strip()
        productTypeId = request.POST['product_typeId']
        productCategoryId = request.POST['product_categoryId']
        productValue = request.POST['product_value']

        productAdd = ProductMaster(
            product_name=productName,
            product_value_on=productValue,
            created_by=request.user
        )

        productType = ProductTypes.objects.get(product_type_id=productTypeId)
        productCategory = ProductCategories.objects.get(product_category_id=productCategoryId)

        productAdd.product_typeId = productType
        productAdd.product_categoryId = productCategory

        productAdd.save()

        messages.success(request, "Product Name: {} added to the database.".format(productName))
        return redirect('product_list')

    context = {
        'productTypeData': productTypeData,
        'ProductCategoriesData': ProductCategoriesData
    }

    return render(request, 'product/product_add.html', context)




def ProductEdit(request,id):
    productTypeList = ProductTypes.objects.all()
    productCategoryList = ProductCategories.objects.all()
    productDataEdit = ProductMaster.objects.get(product_id=id)

    context = {
        'productTypeList': productTypeList,
        'productCategoryList' : productCategoryList,
        'productDataEdit' : productDataEdit
    }
    return render(request, 'product/product_edit.html', context)



def ProductUpdate(request):
    if request.method == "POST":
        productId = request.POST['product_id']
        productName = request.POST['product_name']
        productTypeId = request.POST['product_typeId']
        productCategoryId = request.POST['product_categoryId']   
        productValue = request.POST['product_value'] 
        user = request.user

        productType = ProductTypes.objects.get(product_type_id=productTypeId)
        productCategory = ProductCategories.objects.get(product_category_id=productCategoryId)

        productUpdate = ProductMaster.objects.get(product_id=productId)
        productUpdate.product_name = productName
        productUpdate.product_value_on = productValue
        productUpdate.last_modified_by = user
        productUpdate.product_typeId = productType
        productUpdate.product_categoryId = productCategory
        productUpdate.save()

        messages.success(request, "Product Name:  {} Update in the database.".format(productName))
        return redirect('product_list')
    


def ProductDelete(request,id):
    productDelete = ProductMaster.objects.get(product_id=id)

    productDelete.is_deleted = True
    productDelete.deleted_by = request.user
    productDelete.save()
    
    return redirect('product_list')




def ProductRateList(request):
    productRateList = ShopProductRates.objects.filter(is_deleted = False)
    context = {
        "productRateList" : productRateList
    }
    return render(request, "product_rate/product_rate_list.html", context)




def ProductRateAdd(request):
    shopModelData = ShopModel.objects.all()
    associationData = Associations.objects.all()
    productMasterData = ProductMaster.objects.all()

    if request.method=="POST":
        shopCodeId = request.POST['shop_codeId']
        associationId = request.POST['associationId']
        productId = request.POST['productId']
        rateMargin = request.POST['rate_margin']
        flexibleRate = request.POST['flexible_rate']
        flexibleFormula = request.POST['flexible_formula']  

        shopCode = ShopModel.objects.get(shop_id=shopCodeId)
        association = Associations.objects.get(association_id=associationId)
        productMaster = ProductMaster.objects.get(product_id=productId)

        shopProductRateAdd = ShopProductRates(
            shopId = shopCode,
            associationId = association,
            ProductId = productMaster,
            rate_margin = rateMargin,
            flexible_yn = flexibleRate,
            flexible_formula = flexibleFormula,
            created_by = request.user,
            last_modified_by = request.user
        )
        shopProductRateAdd.save()

        messages.success(request, "Product Rate:  {} Added in the database.".format(rateMargin))
        return redirect('product_rate_list')

    context = {
        "shopModelData" : shopModelData,
        "associationData" : associationData,
        "productMasterData" : productMasterData
    }
    return render(request, 'product_rate/product_rate_add.html', context)



def ProductRateEdit(request,id):

    shopModalData = ShopModel.objects.all()
    associationsData  =Associations.objects.all()
    productData = ProductMaster.objects.all()
    productRateEdit = ShopProductRates.objects.get(shop_product_rates_id=id)

    context ={
        'shopModalData' : shopModalData,
        'associationsData' : associationsData,
        'productData' : productData,
        'productRateEdit' : productRateEdit,
    }
    return render(request, 'product_rate/product_rate_edit.html', context)



def ProductRateUpdate(request):
    if request.method=="POST":
        productRateId = request.POST['product_rate']
        shopCodeId = request.POST['shop_codeId']
        associationId = request.POST['associationId']
        productId = request.POST['productId']
        rateMargin = request.POST['rate_margin']
        flexibleRate = request.POST['flexible_rate']
        flexibleFormula = request.POST['flexible_formula']  

        shopCode = ShopModel.objects.get(shop_id = shopCodeId)
        associations = Associations.objects.get(association_id = associationId)
        product  =ProductMaster.objects.get(product_id = productId)

        shopProductRateUpdate = ShopProductRates.objects.get(shop_product_rates_id = productRateId)
        shopProductRateUpdate.shopId = shopCode
        shopProductRateUpdate.associationId = associations
        shopProductRateUpdate.ProductId = product
        shopProductRateUpdate.rate_margin = rateMargin
        shopProductRateUpdate.flexible_yn = flexibleRate
        shopProductRateUpdate.flexible_formula = flexibleFormula
        shopProductRateUpdate.last_modified_by = request.user
        shopProductRateUpdate.save()

        messages.success(request, "Product Rate Updated Succesfully.")
        return redirect('product_rate_list')
    


def ProductRateDelete(request,id):
    productRateDelete = ShopProductRates.objects.get(shop_product_rates_id = id)

    productRateDelete.is_deleted = True
    productRateDelete.deleted_by = request.user
    productRateDelete.save()

    return redirect('product_rate_list')




# ========================== Shop Balance ===========================


def ShopBalanceList(request):
    shopBalanceList = ShopBalance.objects.filter(is_deleted = False)

    context={
        'shopBalanceList' : shopBalanceList
    }
    return render(request, 'shops/shop_balance_list.html', context)




def ShopBalanceAdd(request):
    shopModelData = ShopModel.objects.all()

    if request.method == "POST":
        shopId = request.POST['shop_id']
        balanceDate = request.POST['balance_date']
        balance = request.POST['balance']
        status = request.POST['status']
        adjustmentAmount = request.POST['adjustment_amount']
        adjustmentRemark = request.POST['adjustment_remark']

        print(shopId, balanceDate, balance, status, adjustmentAmount, adjustmentRemark)

        shopId = ShopModel.objects.get(shop_id = shopId)

        shopBalanceAdd = ShopBalance(
            shopId = shopId,
            balance_date = balanceDate,
            balance = balance,
            active = status,
            adjustment_amount = adjustmentAmount,
            adjustment_remark = adjustmentRemark,
            created_by = request.user
        )
        shopBalanceAdd.save()

        messages.success(request, "Shop Balance Added Succesfully...!")
        return redirect('shop_balance_list')

    context = {
        'shopModelData' : shopModelData
    }
    return render(request, 'shops/shop_balance_add.html', context)




def ShopBalanceEdit(request,id =None):
    shopModelData = ShopModel.objects.all()
    shopBalanceEdit = ShopBalance.objects.get(shop_balance_id = id)

    if request.method == "POST":
        shopId = request.POST['shop_id']
        balanceDate = request.POST['balance_date']
        balance = request.POST['balance']
        status = request.POST['status']
        adjustmentAmount = request.POST['adjustment_amount']
        adjustmentRemark = request.POST['adjustment_remark']

        shopId = ShopModel.objects.get(shop_id = shopId)

        shopBalanceEdit.shopId = shopId
        shopBalanceEdit.balance_date = balanceDate
        shopBalanceEdit.balance = balance
        shopBalanceEdit.active = status
        shopBalanceEdit.adjustment_amount = adjustmentAmount
        shopBalanceEdit.adjustment_remark = adjustmentRemark
        shopBalanceEdit.last_modified_by = request.user
        shopBalanceEdit.save()

        messages.success(request, "Shop Balance Updated Succesfully...!")
        return redirect('shop_balance_list')

    context = {
        'shopModelData' : shopModelData,
        'shopBalanceEdit' : shopBalanceEdit
    }
    return render(request, 'shops/shop_balance_edit.html', context)



def ShopBalanceDelete(request,id):
    shopBalanceDelete = ShopBalance.objects.get(shop_balance_id = id)

    shopBalanceDelete.is_deleted = True
    shopBalanceDelete.deleted_by = request.user
    shopBalanceDelete.save()

    messages.success(request, "Shop Balance Deleted Succesfully...!")
    return redirect('shop_balance_list')



def ShopAndBalanceDetail(request,id):
    shopAndBalance = ShopBalance.objects.get(shop_balance_id = id)
    context ={
        'shopAndBalance' : shopAndBalance
    }
    return render(request, 'shops/shop_and_balance_detail.html', context) 

 


# ===========================  Shop Flexible Rate ==========================


def ShopFlexibleRateList(request):
    shopFlexibleRateList = ShopFlexibleRate.objects.filter(is_deleted = False)

    context ={
        'shopFlexibleRateList' : shopFlexibleRateList
    }
    return render(request, 'shops/shop_flexible_rate_list.html', context) 




def ShopFlexibleRateAdd(request):
    shopModelData = ShopModel.objects.all()
    productTypeData = ProductTypes.objects.all()

    if request.method == "POST":
        rateDate = request.POST['shop_flexible_date']
        shopId = request.POST['shop_id']
        productTypeId = request.POST['product_type_id']
        flexibleRate = request.POST['flexible_rate']
        flexibleFormula = request.POST['flexible_formula']
        sellRate = request.POST['sell_rate']
        withSkin = request.POST['with_skin']
        withoutSkin = request.POST['without_skin']
        smsSendYN = request.POST['sms_send_yn']
        smsReplyId = request.POST['sms_replyId']

        print(rateDate, shopId, productTypeId,flexibleRate, flexibleFormula,  sellRate, withSkin, withoutSkin, smsSendYN,smsReplyId )

        shopId = ShopModel.objects.get(shop_id=shopId)
        productTypeId = ProductTypes.objects.get(product_type_id=productTypeId)

        shopFlexibleRateAdd = ShopFlexibleRate(
            flexible_rate_date = rateDate,
            shopId = shopId,
            product_typeId = productTypeId,
            flexible_rate = flexibleRate,
            flexible_formula = flexibleFormula,
            sell_rate = sellRate,
            with_skin = withSkin,
            without_skin = withoutSkin,
            sms_send_yn = smsSendYN,
            sms_replyId = smsReplyId,
            created_by = request.user
        )
        shopFlexibleRateAdd.save()

        messages.success(request, "Shop Flexible Rate Added Succesfully...!")
        return redirect('shop_flexible_rate_list')

    context = {
        'shopModelData' : shopModelData,
        'productTypeData' : productTypeData
    }

    return render(request, 'shops/shop_flexible_rate_add.html', context) 



def ShopFlexibleRateEdit(request,id):
    shopModelData = ShopModel.objects.all()
    productTypeData = ProductTypes.objects.all()

    shopFlexibleRateEdit = ShopFlexibleRate.objects.get(shop_flexible_rate_id = id)

    if request.method == "POST":
        rateDate = request.POST['shop_flexible_date']
        shopId = request.POST['shop_id']
        productTypeId = request.POST['product_type_id']
        flexibleRate = request.POST['flexible_rate']
        flexibleFormula = request.POST['flexible_formula']
        sellRate = request.POST['sell_rate']
        withSkin = request.POST['with_skin']
        withoutSkin = request.POST['without_skin']
        smsSendYN = request.POST['sms_send_yn']
        smsReplyId = request.POST['sms_replyId']

        print(rateDate, shopId, productTypeId,flexibleRate, flexibleFormula,  sellRate, withSkin, withoutSkin, smsSendYN,smsReplyId )

        shopId = ShopModel.objects.get(shop_id=shopId)
        productTypeId = ProductTypes.objects.get(product_type_id=productTypeId)

        shopFlexibleRateEdit.flexible_rate_date = rateDate
        shopFlexibleRateEdit.shopId = shopId
        shopFlexibleRateEdit.product_typeId = productTypeId
        shopFlexibleRateEdit.flexible_rate = flexibleRate
        shopFlexibleRateEdit.flexible_formula = flexibleFormula
        shopFlexibleRateEdit.sell_rate = sellRate
        shopFlexibleRateEdit.with_skin = withSkin
        shopFlexibleRateEdit.without_skin = withoutSkin
        shopFlexibleRateEdit.sms_send_yn = smsSendYN
        shopFlexibleRateEdit.sms_replyId = smsReplyId
        shopFlexibleRateEdit.last_modified_by = request.user
        shopFlexibleRateEdit.save()

        messages.success(request, "Shop Flexible Rate Updated Succesfully...!")
        return redirect('shop_flexible_rate_list')

    context = {
        'shopModelData' : shopModelData,
        'productTypeData' : productTypeData,
        'shopFlexibleRateEdit' : shopFlexibleRateEdit
    }

    return render(request, 'shops/shop_flexible_rate_edit.html', context)



def ShopFlexibleRateDelete(request,id):
    shopFlexibleRateDelete = ShopFlexibleRate.objects.get(shop_flexible_rate_id = id)

    shopFlexibleRateDelete.is_deleted = True
    shopFlexibleRateDelete.deleted_by = request.user
    shopFlexibleRateDelete.save()

    messages.success(request, "Shop Flexible Rate Deleted Succesfully...!")
    return redirect('shop_flexible_rate_list')



##################################

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
        