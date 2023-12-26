from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserRole(models.Model):
    user_role_id = models.AutoField(primary_key=True)
    user_role_name = models.CharField(max_length=100)

    def __str__(self):
        return self.user_role_name


class UserModel(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    user_mobile_no = models.CharField(max_length=15)
    user_alt_mobile_no = models.CharField(max_length=15)
    user_password = models.CharField(max_length=100)
    user_role = models.ForeignKey(UserRole, on_delete=models.SET_NULL, null=True)
    user_level = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='user_model_created_by')
    last_modified_on = models.DateTimeField(auto_now=True)
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='user_model_last_modified')
    is_deleted = models.BooleanField(default=False)
    deleted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='user_model_deleted')


    def __str__(self):
        return self.user_name
