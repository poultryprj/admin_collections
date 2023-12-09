from django.shortcuts import redirect, render
from shop.models import ProductTypes
from django.contrib import messages
from .models import Vendor, VendorProduct
# Create your views here.


def VendorList(request):
    vendorList = Vendor.objects.filter(is_deleted = False)

    context = {
        'vendorList' : vendorList
    }
    return render(request, 'vendor/vendor_list.html', context)




def VendorAdd(request):
    productTypesData = ProductTypes.objects.all()

    if request.method  == "POST":
        vendorName = request.POST['vendor_name'].capitalize().strip()
        vendorCode = request.POST['vendor_code']
        productType = request.POST['product_type']
        vendorCompany = request.POST['vendor_company'].capitalize().strip()
        vendorContactNo = request.POST['contactNo']
        vendorAltContactNo = request.POST['alt_contactNo']
        vendorAddress = request.POST['address'].capitalize().strip()
        vendorStatus = request.POST['status']

        print(vendorName, productType, vendorCompany, vendorContactNo, vendorAltContactNo, vendorAddress, vendorStatus)

        vendorAdd = Vendor(
            vendor_name = vendorName,
            vendor_code = vendorCode,
            vendor_type = productType,
            vendor_company = vendorCompany,
            vendor_contactNo = vendorContactNo,
            vendor_alternateNo = vendorAltContactNo,
            vendor_address = vendorAddress,
            vendor_active = vendorStatus,
            created_by = request.user,
        )
        vendorAdd.save()

        messages.success(request, "Vendor Name {} Added Successfully...".format(vendorName))
        return redirect('vendor_list')

    context = {
        'productTypesData' : productTypesData
    }
    return render(request, 'vendor/vendor_add.html', context) 



def VendorEdit(request, id):
    productTypesData = ProductTypes.objects.all()

    vendorEdit = Vendor.objects.get(vendor_id = id)

    if request.method == "POST":
        vendorName = request.POST['vendor_name'].capitalize().strip()
        vendorCode = request.POST['vendor_code']
        productType = request.POST['product_type']
        vendorCompany = request.POST['vendor_company'].capitalize().strip()
        vendorContactNo = request.POST['contactNo']
        vendorAltContactNo = request.POST['alt_contactNo']
        vendorAddress = request.POST['address'].capitalize().strip()
        vendorStatus = request.POST['status']

        print(vendorName, productType, vendorCompany, vendorContactNo, vendorAltContactNo, vendorAddress, vendorStatus)

        vendorEdit.vendor_name = vendorName
        vendorEdit.vendor_code = vendorCode
        vendorEdit.vendor_type =productType
        vendorEdit.vendor_company = vendorCompany
        vendorEdit.vendor_contactNo = vendorContactNo
        vendorEdit.vendor_alternateNo = vendorAltContactNo
        vendorEdit.vendor_address = vendorAddress
        vendorEdit.vendor_active = vendorStatus
        vendorEdit.last_modified_by = request.user
        vendorEdit.save()

        messages.success(request, "Vendor Name {} Updated Successfully.".format(vendorName))
        return redirect('vendor_list')

    context = {
        'vendorEdit' : vendorEdit,
        'productTypesData' : productTypesData
    }
    return render(request, 'vendor/vendor_edit.html', context)




def VendorDelete(request,id):
    vendorDelete = Vendor.objects.get(vendor_id = id)
    vendorDelete.is_deleted = True
    vendorDelete.deleted_by = request.user
    vendorDelete.save()

    messages.success(request, "Vendor Name {} Deleted Successfully.".format(vendorDelete.vendor_name))
    return redirect('vendor_list')



# ========================================== Vendor Product =======================================


def VendorProductAdd(request):
    vedorData = Vendor.objects.filter(is_deleted=False)
    productTypesData = ProductTypes.objects.all()
    
    if request.method == "POST":
        vendorId = request.POST['vendor_id']
        productTypeId = request.POST['product_type_id']
        productRate = request.POST['product_rate']
        productTCS = request.POST['product_tcs']
        productTDS = request.POST['product_tds']

        print(vendorId, productTypeId, productRate, productTCS, productTDS)

       

    context = {
        'vedorData' : vedorData,
        'productTypesData' : productTypesData
    }
    return render(request, 'vendor/vendor_product_add.html',context)