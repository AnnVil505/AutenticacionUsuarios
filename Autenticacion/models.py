from django.db import models
from django.contrib.auth.models import User

# Role table creation
class Role(models.Model):
    id_role = models.BigAutoField(primary_key=True)
    name_role = models.CharField(max_length=40)
    description_role = models.TextField(max_length=1000)
    date_role = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id_role + ' - ' + self.date_role

    def __repr__(self):
        return self.name_role

# Permission table creation
class Permission(models.Model):
    id_permission = models.BigAutoField(primary_key=True)
    name_permission = models.CharField(max_length=100)
    description_permission = models.TextField(max_length=1000)
    date_permission = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id_permission + ' - ' + self.date_permission
    
    def __repr__(self):
        return self.name_permission

# Role_Permission table creation
class Role_Permission(models.Model):
    id_role_permission = models.BigAutoField(primary_key=True)
    id_role_FK = models.ForeignKey(Role, on_delete=models.CASCADE)
    id_permission_FK = models.ForeignKey(Permission, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_role_permission + ' - ' + self.id_permission_FK

# Role_User table creation
class Role_User(models.Model):
    id_role_user = models.BigAutoField(primary_key=True)
    id_user_FK = models.ForeignKey(User, on_delete=models.CASCADE)
    id_role_FK = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_role_user + ' - ' + self.id_role_FK
