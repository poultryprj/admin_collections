from django.db import models
from django.contrib.auth.models import User

class RouteModel(models.Model):
    route_id = models.AutoField(primary_key=True)
    route_name = models.CharField(max_length=100)
    route_start_point = models.CharField(max_length=100)
    route_end_point = models.CharField(max_length=100)
    route_areas = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='routes_route_model')
    last_modified_on = models.DateTimeField(auto_now=True)
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='RouteModel_last_modified_by')
    is_deleted = models.BooleanField(default=False)
    deleted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='RouteModel_deleted')


    def __str__(self):
        return self.route_name   
    
    class Meta:
        db_table = "RouteModel"