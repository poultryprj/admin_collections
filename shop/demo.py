# Python script to save data into the database from a JSON file

import json
from .models import ShopModel, ShopOwner

def save_shop_data_from_json(file_path):
    with open(file_path, 'r') as file:
        json_data = json.load(file)
        shop_owner_data = ShopOwner.objects.all()
        
        for data in json_data:
           
            shopCode = data.get('shop_code')
            shopName = data.get('shop_name')
            shopArea = data.get('shop_area')
            shopLatitude = data.get('shop_latitude')
            shopLongitude = data.get('shop_longitude')
            shopAddress = data.get('shop_address')
            shopPinCode = data.get('shop_pincode')
            shopDistance = data.get('shop_distance')
            shopMobileNo = data.get('shop_mobileNo')
            shopAlternateNo = data.get('shop_alternateNo')
            shopOwnerId = data.get('shop_ownerId')
            shoptype = data.get('shop_type')
            shopStatus = data.get('shop_status')


           
            owner_instance = ShopOwner.objects.get(owner_id=shopOwnerId)

            # Create a ShopModel instance with extracted data
            shop_add = ShopModel(

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
                shop_ownerId = owner_instance,
                shop_type = shoptype,
                shop_status = shopStatus,

            )
            shop_add.save()

# Usage: Replace 'file_path' with the path to your JSON file
save_shop_data_from_json('path_to_your_json_file.json')
