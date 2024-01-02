from django.shortcuts import redirect, render
from shop.models import ProductTypes
from django.contrib import messages
from .models import Vendor, VendorCreditBalance, VendorOpeningBalance, VendorProduct
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


def VendorProductList(request):
    vendorProducts = VendorProduct.objects.filter(is_deleted = False)

    context = {
        'vendorProducts' : vendorProducts
    }
    return render(request, 'vendor/vendor_product_list.html', context)



def VendorProductAdd(request):
    vendorData = Vendor.objects.filter(is_deleted=False)
    productTypesData = ProductTypes.objects.all()
    
    if request.method == "POST":
        vendorId = request.POST['vendor_id']
        productTypeId = request.POST['product_type_id']
        productRate = request.POST['product_rate']
        productTCS = request.POST['product_tcs']
        productTDS = request.POST['product_tds']

        vendorId = Vendor.objects.get(vendor_id = vendorId)
        productTypeId = ProductTypes.objects.get(product_type_id = productTypeId)

        vendorProductAdd = VendorProduct(
            vendorId = vendorId,
            productId = productTypeId,
            product_rate = productRate,
            product_tcs = productTCS,
            product_tds = productTDS,
            created_by = request.user
        )
        vendorProductAdd.save()

        messages.success(request, "Added Successfully.")
        return redirect('vendor_product_list')
       
    context = {
        'vendorData' : vendorData,
        'productTypesData' : productTypesData
    }
    return render(request, 'vendor/vendor_product_add.html',context)




def VendorProductEdit(request,id):
    vendorData = Vendor.objects.filter(is_deleted=False)
    productTypesData = ProductTypes.objects.all()
    
    vendorProductEdit = VendorProduct.objects.get(vender_product_id = id)

    if request.method == "POST":
        vendorId = request.POST['vendor_id']
        productTypeId = request.POST['product_type_id']
        productRate = request.POST['product_rate']
        productTCS = request.POST['product_tcs']
        productTDS = request.POST['product_tds']

        vendorId = Vendor.objects.get(vendor_id = vendorId)
        productTypeId = ProductTypes.objects.get(product_type_id = productTypeId)

        vendorProductEdit.vendorId = vendorId
        vendorProductEdit.productId = productTypeId
        vendorProductEdit.product_rate = productRate
        vendorProductEdit.product_tcs = productTCS
        vendorProductEdit.product_tds = productTDS
        vendorProductEdit.last_modified_by = request.user
        vendorProductEdit.save()

        messages.success(request, "Updated Successfully.")
        return redirect('vendor_product_list')
    
    context = {
         'vendorData' : vendorData,
         'productTypesData' : productTypesData,
         'vendorProductEdit' : vendorProductEdit
     }
    return render(request, 'vendor/vendor_product_edit.html',context)




def VendorProductDelete(request,id):
    vendorProductDelete = VendorProduct.objects.get(vender_product_id = id)

    vendorProductDelete.is_deleted = True
    vendorProductDelete.deleted_by = request.user
    vendorProductDelete.save()

    messages.success(request, "Deleted Successfully..")
    return redirect('vendor_product_list')



# ================================== Vendor Opening Balance =====================================


def VendorOpeningBalanceList(request):
    vendorOpeningBalances = VendorOpeningBalance.objects.filter(is_deleted=False)
    context = {
        'vendorOpeningBalances' : vendorOpeningBalances
    }
    return render(request, 'vendor/vendor_opening_balance_list.html', context)



def VendorOpeningBalanceAdd(request):
    vendorData = Vendor.objects.filter(is_deleted=False)

    if request.method == "POST":
        vendorId = request.POST['vendor_id']
        balanceDate = request.POST['balance_date']
        balance = request.POST['balance']
        active = request.POST['active']
        adjustmentAmout = request.POST['adjustment_amount']
        adjustmentRemark = request.POST['adjustment_remark']

        vendorId = Vendor.objects.get(vendor_id = vendorId)

        vendorOpeningBalanceAdd = VendorOpeningBalance(
            vendorId = vendorId,
            balance_date = balanceDate,
            balance = balance,
            active  = active,
            adjustment_amount = adjustmentAmout,
            adjustment_remark = adjustmentRemark,
            created_by = request.user
        )
        vendorOpeningBalanceAdd.save()

        messages.success(request, "Added Successfully..")
        return redirect('vendor_opening_balance_list')

    context = {
        'vendorData' : vendorData
    }
    return render(request, 'vendor/vendor_opening_balance_add.html', context)




def VendorOpeningBalanceEdit(request,id):
    vendorData = Vendor.objects.filter(is_deleted=False)

    vendorOpeningBalanceEdit = VendorOpeningBalance.objects.get(vendor_opening_balance_id = id)

    if request.method == "POST":
        vendorId = request.POST['vendor_id']
        balanceDate = request.POST['balance_date']
        balance = request.POST['balance']
        active = request.POST['active']
        adjustmentAmout = request.POST['adjustment_amount']
        adjustmentRemark = request.POST['adjustment_remark']

        vendorId = Vendor.objects.get(vendor_id = vendorId)

        vendorOpeningBalanceEdit.vendorId = vendorId
        vendorOpeningBalanceEdit.balance_date = balanceDate
        vendorOpeningBalanceEdit.balance = balance
        vendorOpeningBalanceEdit.active = active
        vendorOpeningBalanceEdit.adjustment_amount = adjustmentAmout
        vendorOpeningBalanceEdit.adjustment_remark = adjustmentRemark
        vendorOpeningBalanceEdit.last_modified_by = request.user
        vendorOpeningBalanceEdit.save()

        messages.success(request, "Updated Successfully.")
        return redirect('vendor_opening_balance_list')

    context = {
        'vendorData' : vendorData,
        'vendorOpeningBalanceEdit' : vendorOpeningBalanceEdit
    }
    return render(request, 'vendor/vendor_opening_balance_edit.html', context)



def VendorOpeningBalanceDelete(request,id):
    vendorOpeningBalanceDelete = VendorOpeningBalance.objects.get(vendor_opening_balance_id = id)

    vendorOpeningBalanceDelete.is_deleted = True
    vendorOpeningBalanceDelete.deleted_by = request.user
    vendorOpeningBalanceDelete.save()

    messages.success(request, "Deleted Successfully..")
    return redirect('vendor_opening_balance_list')



# ================================== Vendor Credit Balance =====================================

def VendorCreditBalanceList(request):

    vendorCreditBalances = VendorCreditBalance.objects.filter(is_deleted = False)

    context = {
        'vendorCreditBalances' : vendorCreditBalances
    }

    return render(request, 'vendor/vendor_credit_balance_list.html', context)




def VendorCreditBalanceAdd(request):
    vendorData = Vendor.objects.filter(is_deleted=False)

    if request.method == "POST":
        vendorId = request.POST['vendor_id']
        amount = request.POST['amount']
        reason = request.POST['reason']
        credit_date = request.POST['credit_date']

        print(vendorId, amount, reason, credit_date)

        vendorId = Vendor.objects.get(vendor_id = vendorId)

        vendorCreditBalanceAdd = VendorCreditBalance(
            vendorId = vendorId,
            amount = amount,
            reason = reason,
            credit_date = credit_date
        )
        vendorCreditBalanceAdd.save()

        messages.success(request, "Credit Balance Added Successfully..")
        return redirect('vendor_credit_balance_list')


    context = {
        'vendorData' : vendorData,
    }
    return render(request, 'vendor/vendor_credit_balance_add.html', context)




def VendorCreditBalanceEdit(request,id):
    vendorData = Vendor.objects.filter(is_deleted=False)

    vendorCreditBalanceEdit = VendorCreditBalance.objects.get(vendor_credit_balance_id = id)

    if request.method == "POST":
        vendorId = request.POST['vendor_id']
        amount = request.POST['amount']
        reason = request.POST['reason']
        credit_date = request.POST['credit_date']

        print(vendorId, amount, reason, credit_date)

        vendorId = Vendor.objects.get(vendor_id = vendorId)

        vendorCreditBalanceEdit.vendorId = vendorId
        vendorCreditBalanceEdit.amount = amount
        vendorCreditBalanceEdit.reason = reason
        vendorCreditBalanceEdit.credit_date = credit_date
        vendorCreditBalanceEdit.save()

        messages.success(request, "Credit Balance Updated Successfully..")
        return redirect('vendor_credit_balance_list')

    context = {
            'vendorData' : vendorData,
            'vendorCreditBalanceEdit' : vendorCreditBalanceEdit
        }

    return render(request, 'vendor/vendor_credit_balance_edit.html', context)


def VendorCreditBalanceDelete(request,id):
    vendorCreditBalanceDelete = VendorCreditBalance.objects.get(vendor_credit_balance_id = id)
    vendorCreditBalanceDelete.is_deleted = True

    messages.success(request, "Credit Balance Deleted Successfully..")
    return redirect('vendor_credit_balance_list')



