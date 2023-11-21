from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import  ShopModel, ShopOwner, ShopRoute
from routes.models import RouteModel

# Create your views here.



def ShopList(request):
    shopLists = ShopModel.objects.filter(is_deleted=False)
    return render(request, 'shops/shop_list.html', context={'shopLists': shopLists})



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

# *******************
def AllShopList(request):
    # selected_shops = ShopModel.objects.filter(pk__in=selected_shop_ids)
    # print(selected_shops)
    return render(request, 'shop_routes/all_shop_list.html')
# **********************
from django.http import JsonResponse
from django.shortcuts import render
from .models import RouteModel, ShopModel, ShopRoute

def RouteList(request):
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