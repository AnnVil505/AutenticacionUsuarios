from django.forms import ModelForm
from .models import Role, Permission, Role_User, Role_Permission

class RoleForm(ModelForm):
    class Meta:
        model = Role
        fields = ['name_role', 'description_role']

class PermissionForm(ModelForm):
    class Meta:
        model = Permission
        fields = ['name_permission', 'description_permission']

class UserRoleForm(ModelForm):
    class Meta:
        model = Role_User
        fields = ['id_user_FK', 'id_role_FK']