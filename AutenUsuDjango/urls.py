from django.contrib import admin
from django.urls import path
from Autenticacion import views
from Autenticacion.DAO.UserDAO import signup, view_user, delete_user, create_user
from Autenticacion.DAO.RoleDAO import create_role, view_roles, delete_role, role_detail
from Autenticacion.DAO.PermissionDAO import create_permission, view_permission, permission_detail, delete_permission
from Autenticacion.DAO.RolePermissionDAO import view_role_permission, delete_role_permission, assign_permission
from Autenticacion.DAO.UserRoleDAO import view_role_user, delete_role_user, assign_role

urlpatterns = [
    path("", views.home, name="home"),
    path("admin/", admin.site.urls),
    path('signin/', views.signin, name='signin'),
    path("Authentication/", views.authentication , name="authentication"),
    path('logout/', views.signout, name='logout'),
    path('user/', view_user, name='users'),
    path('create_user/', signup, name='signup'),
    path('create_user/', create_user, name="Cuser"),
    path('user/<str:user_name>/delete', delete_user, name='delete_user'),
    path('roles/', view_roles, name='roles'),
    path('create_role/', create_role, name='Crole'),
    path('roles/<int:role_id>', role_detail, name='role_detail'),
    path('roles/<int:role_id>/delete', delete_role, name='delete_role'),
    path('permissions/', view_permission, name='permissions'),
    path('create_permission/', create_permission, name='Cpermission'),
    path('permission/<int:permission_id>', permission_detail, name='permission_detail'),
    path('permission/<int:permission_id>/delete', delete_permission, name='delete_permission'),
    path('roles/AssignPermissions/<int:role_id>', view_role_permission, name='assignPermission'),
    path('roles/AssignPermissions/<int:role_id>/<int:permission_id>/delete', delete_role_permission, name='delete_role_permission'),
    path('roles/AssignPermissions/<int:role_id>/<int:permission_id>/add', assign_permission, name='assign_role_permission'),
    path('user/AssignRoles/<str:user_username>', view_role_user, name='assignRole'),
    path('user/AssignRoles/<str:user_username>/delete', delete_role_user, name='delete_role_user'),
    path('user/AssignRoles/<str:user_username>/<int:role_id>/add', assign_role, name='assign_role_user'),
]


