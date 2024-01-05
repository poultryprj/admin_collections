from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import RouteModel

def RouteList(request):
    routes = RouteModel.objects.filter(is_deleted=False)

    return render(request, 'routes/route_list.html', context={'routes': routes})


def RouteAdd(request):
    if request.method == "POST":
        routeName = request.POST['route_name'].capitalize()
        routeStartPoint = request.POST['route_start_point']
        routeEndPoint = request.POST['route_end_point']
        routeAreas = request.POST['route_areas']

        existing_route = RouteModel.objects.filter(route_name=routeName).first()

        if existing_route:
            messages.error(request, "Route with name {} already exists.".format(routeName))
            return redirect("route_list")  
        else:
            addRoute = RouteModel(
                route_name=routeName,
                route_start_point=routeStartPoint,
                route_end_point=routeEndPoint,
                route_areas=routeAreas,
                created_by=request.user,
                last_modified_by=request.user
            )
            addRoute.save()

            messages.success(request, "Route Name: {} added to the database.".format(routeName))
            return redirect("route_list")

    return render(request, 'routes/route_add.html')



def RouteEdit(request,id):

    routeData = RouteModel.objects.get(route_id=id)

    return render(request, 'routes/route_edit.html', context={'routeData': routeData})


def RouteUpdate(request):
    if request.method == "POST":
        routePk = request.POST['routePk']
        routeId = int(request.POST['route_id'])
        routeName = request.POST['route_name'].capitalize()
        routeStartPoint = request.POST['route_start_point']
        routeEndPoint = request.POST['route_end_point']
        routeAreas = request.POST['route_areas']
        

        routeUpdate = get_object_or_404(RouteModel, route_id=routeId)
        
        existing_route = RouteModel.objects.filter(route_name__iexact=routeName).exclude(route_id=routeId).first()
        
        if existing_route:
            messages.error(request, "Route with name '{}' already exists.".format(routeName))
            return redirect("route_list") 
        else:
            routeUpdate.route_name = routeName
            routeUpdate.route_start_point = routeStartPoint
            routeUpdate.route_end_point = routeEndPoint
            routeUpdate.route_areas = routeAreas
            routeUpdate.last_modified_by = request.user
            routeUpdate.save()

            messages.success(request, "Route ID {} updated in the database.".format(routeId))
            return redirect('route_list')

    return render(request, 'routes/route_list.html')



def RouteDelete(request ,id):
    routedelete = RouteModel.objects.get(route_id=id)
    routedelete.is_deleted = True
    routedelete.deleted_by=request.user.username
    routedelete.save()
    return redirect('route_list')