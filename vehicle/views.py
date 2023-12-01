import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from vehicle.models import VehicalMakeBy

def VehicleDetailAdd(request):
    vehicalMakeByData = VehicalMakeBy.objects.all()
    context = {'vehicalMakeByData': vehicalMakeByData}
    return render(request, 'vehicle/vehicle_detail_add.html', context)


def vehicalMakeByAdd(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))  # Decode the JSON data
        addName = data.get('new_name')
        if addName:
            try:
                addData = VehicalMakeBy(vehical_make_by=addName)
                addData.save()
                return JsonResponse({'success': True, 'new_name': addName})
    
            except Exception as e:
                return JsonResponse({'success': False, 'error_message': str(e)}, status=500)
            
