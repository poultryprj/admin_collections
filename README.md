from django.shortcuts import render
from .models import AssetPurchase
from datetime import datetime

def add_asset_purchase(request):
    if request.method == 'POST':
        purchase_date = request.POST.get('purchase_date')
        purchase_time = request.POST.get('purchase_time')
        # Retrieve other form data similarly
        
        combined_datetime = datetime.strptime(f'{purchase_date} {purchase_time}', '%Y-%m-%d %H:%M:%S')
        
        asset_purchase = AssetPurchase(
            purchase_on=combined_datetime,
            # Set other fields here
        )
        asset_purchase.save()
        # Handle successful form submission or redirection
        
    return render(request, 'add_asset_purchase.html')




<form method="post">
    {% csrf_token %}
    <label for="id_purchase_date">Purchase Date:</label>
    <input type="date" id="id_purchase_date" name="purchase_date">

    <label for="id_purchase_time">Purchase Time:</label>
    <input type="time" id="id_purchase_time" name="purchase_time">
    
    <!-- Other input fields for the form -->
    
    <button type="submit">Submit</button>
</form>
