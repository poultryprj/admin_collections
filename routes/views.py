from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import RouteModel

# Create your views here.


def RouteList(request):
    routes = RouteModel.objects.filter(is_deleted=False)

    return render(request, 'routes/route_list.html', context={'routes': routes})


def RouteAdd(request):
    if request.method == "POST":
        routeName = request.POST['route_name']
        routeStartPoint = request.POST['route_start_point']
        routeEndPoint = request.POST['route_end_point']
        routeAreas = request.POST['route_areas']

        addRoute = RouteModel(
        route_name = routeName,
        route_start_point = routeStartPoint,
        route_end_point = routeEndPoint,
        route_areas = routeAreas,
        created_by = request.user,
        last_modified_by = request.user
        )
        addRoute.save()

        messages.success(request, "Route Name: {} Add in the database.".format(routeName))
        return redirect("route_list")

    return render(request, 'routes/route_add.html')



def RouteEdit(request,id):

    routeData = RouteModel.objects.get(route_id=id)

    return render(request, 'routes/route_edit.html', context={'routeData': routeData})


def RouteUpdate(request):
    if request.method == "POST":
        routePk = request.POST['routePk']
        routeId = int(request.POST['route_id'])
        routeName = request.POST['route_name']
        routeStartPoint = request.POST['route_start_point']
        routeEndPoint = request.POST['route_end_point']
        routeAreas = request.POST['route_areas']
        user = request.user.username

        routeUpdate = RouteModel.objects.get(route_id=routeId)
        routeUpdate.route_name = routeName
        routeUpdate.route_start_point = routeStartPoint
        routeUpdate.route_end_point = routeEndPoint
        routeUpdate.route_areas = routeAreas
        routeUpdate.last_modified_by = user
        routeUpdate.save()
    
        messages.success(request, "Route ID {} Update in the database.".format(routeId))
        return redirect('route_list')



def RouteDelete(request ,id):
    routedelete = RouteModel.objects.get(route_id=id)
    routedelete.is_deleted = True
    routedelete.deleted_by=request.user.username
    routedelete.save()
    return redirect('route_list')