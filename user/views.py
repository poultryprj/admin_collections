from django.shortcuts import render, HttpResponse, redirect
from .models import UserModel
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

def UserList(request):
    userList = UserModel.objects.filter(is_deleted=False)
    context = {
        'userList': userList
    }
    return render(request, 'users/users_list.html', context)



def AddUser(request):
    if request.method == 'POST':
        userName = request.POST['user_name']
        userMobileNo = request.POST['user_mobile_no']
        userAltMobileNo = request.POST['user_alt_mobile_no']
        userPassword = request.POST['user_password']
        userLevel = request.POST['user_level']
        
        addUser = UserModel(
            user_name  = userName,
            user_mobile_no = userMobileNo, 
            user_alt_mobile_no = userAltMobileNo,
            user_password = userPassword,
            user_level = userLevel,
            created_by = request.user
        )
        addUser.save()

        messages.success(request, "User Name: {} Add in the database.".format(userName))
        return redirect("user_list")

    return render(request, 'users/user_add.html')



def EditUser(request, id):
    editUserData = UserModel.objects.get(user_id=id)

    context = {
        'editUserData': editUserData
    }
    return render(request, 'users/user_edit.html', context)



def UserUpdate(request):
    if request.method == 'POST':
        userId = request.POST['user_id']
        userName = request.POST['user_name']
        userMobileNo = request.POST['user_mobile_no']
        userAltMobileNo = request.POST['user_alt_mobile_no']
        userPassword = request.POST['user_password']
        userLevel = request.POST['user_level']
        
        print(userName, userMobileNo, userAltMobileNo, userPassword, userLevel)

        userUpdateData = UserModel.objects.get(user_id=userId)
        userUpdateData.user_name  = userName
        userUpdateData.user_mobile_no = userMobileNo
        userUpdateData.user_alt_mobile_no = userAltMobileNo
        userUpdateData.user_password = userPassword
        userUpdateData.user_level = userLevel
        userUpdateData.last_modified_by = request.user

        userUpdateData.save()
        messages.success(request, "User Name: {} Update in the database.".format(userName))
        
    return redirect('user_list')



def UserDelete(request,id):
    userDelete = UserModel.objects.get(user_id=id)
    print(userDelete)

    userDelete.is_deleted=True
    userDelete.deleted_by=request.user
    userDelete.save()
    return redirect('user_list')
