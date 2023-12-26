Certainly! Below is a `README.md` file that provides information about the provided Django models, their relationships, and examples to use the endpoints with Postman.

```markdown
# Django Models Documentation

## Collection
- `collection_id`: Auto-incremented primary key
- `collection_date`: Date of the collection
- `collection_time`: Time of the collection
- `shopId`: Foreign key to ShopModel
- `cashierId`: Foreign key to User (related_name='collection_cashier_id')
- `latitude`: Decimal field for latitude
- `longitude`: Decimal field for longitude
- `total_amount`: Float field for total amount
- `fanialize_on`: DateTimeField for finalization timestamp
- `fanialize_by`: Foreign key to User

## CollectionMode
- `collection_mode_id`: Auto-incremented primary key
- `collectionId`: Foreign key to Collection
- `payment_mode`: String field for payment mode
- `payment_amount`: Float field for payment amount
- `upload_image`: FileField for uploaded images

## SkipShop
- `skip_shop_id`: Auto-incremented primary key
- `skip_shop_date`: Date of skip shop
- `skip_shop_time`: Time of skip shop
- `shopId`: Foreign key to ShopModel
- `cashierId`: Foreign key to User (related_name='SkipShop_cashier_Id')
- `approve_yn`: String field for approval status
- `remark`: TextField for remarks
- `approve_byId`: Foreign key to User for approval
- `created_on`: DateTimeField for creation timestamp
- `created_by`: Foreign key to User (related_name='SkipShop_created_by')
- `last_modified_on`: DateTimeField for last modification timestamp
- `last_modified_by`: Foreign key to User (related_name='SkipShop_last_modified_by')

## API Endpoints

### Shop List API
- URL: `/shop_list_api/`
- Method: GET
- Description: Fetches a list of shops

### Collections API
- URL: `/collections_api/`
- Method: POST
- Description: Adds a new collection

### Collection View
- URL: `/collections_view/`
- Method: GET
- Description: View collections

### Collection Mode Add
- URL: `/collection_mode_add/`
- Method: POST
- Description: Adds a new collection mode

### Collection Mode Get
- URL: `/collection_mode_get/<collection_id>/`
- Method: GET
- Description: Retrieves collection modes for a specific collection

## Example Usage with Postman

1. **Add Collection**
   - Endpoint: `/collections_api/`
   - Method: POST
   - Body (JSON):
     ```json
     {
         "collection_date": "2023-12-15",
         "collection_time": "08:30:00",
         "shopId": 1,
         "cashierId": 2,
         "latitude": 40.7128,
         "longitude": -74.0060,
         "total_amount": 100.0
     }
     ```

2. **Add Collection Mode**
   - Endpoint: `/collection_mode_add/`
   - Method: POST
   - Body (Form-Data):
     ```
     collectionId: 1
     payment_mode: "Card"
     payment_amount: 50.0
     upload_image: <Upload an image file>
     ```

3. **Get Collection Modes for Collection ID**
   - Endpoint: `/collection_mode_get/<collection_id>/`
   - Method: GET
   - Replace `<collection_id>` with the actual collection ID
```

This `README.md` provides a summary of your Django models, their relationships, and how to interact with your defined API endpoints using Postman. Adjust the example data and endpoints as needed based on your specific implementation.