from django.contrib import admin
from .models import UserModel, UserRole
# Register your models here.


class UserModelAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user_name', 'user_mobile_no', 'user_alt_mobile_no', 'user_password', 'user_role', 'user_level', 'created_on', 'created_by', 'last_modified_on', 'last_modified_by', 'is_deleted', 'deleted_by')
    
    search_fields = ('user_id','user_name', 'user_role', 'user_level')

    list_display_links = ('user_id','user_name', 'user_mobile_no', 'user_alt_mobile_no', 'user_password','user_role', 'user_level')


class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('user_role_id', 'user_role_name')
    
    search_fields = ('user_role_id','user_role_name')

    list_display_links = ('user_role_id','user_role_name')
    
    

admin.site.register(UserModel,UserModelAdmin)
admin.site.register(UserRole,UserRoleAdmin)