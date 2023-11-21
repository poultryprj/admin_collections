from django.contrib import admin
from .models import UserModel
# Register your models here.


class UserModelAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user_name', 'user_mobile_no', 'user_alt_mobile_no', 'user_password','user_level', 'created_on', 'created_by', 'last_modified_on', 'last_modified_by', 'is_deleted', 'deleted_by')
    search_fields = ('user_id','user_name','user_level')

    list_display_links = ('user_id','user_name', 'user_mobile_no', 'user_alt_mobile_no', 'user_password','user_level')
    
    

admin.site.register(UserModel,UserModelAdmin)