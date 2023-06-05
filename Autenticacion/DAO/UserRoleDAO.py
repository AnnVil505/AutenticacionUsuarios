from django.shortcuts import get_object_or_404, render, redirect
from Autenticacion.forms import UserRoleForm
from Autenticacion.models import Role_User, Role
from django.contrib.auth.models import User

def assign_role(request, user_username, role_id):
    if request.method == 'POST':
        arp = Role_User(id_user_FK=User.objects.get(username=user_username), id_role_FK= Role.objects.get(id_role=role_id))
        arp.save()
        return redirect('users')
        
def view_role_user(request, user_username):  
    if request.method == 'POST':
        id_user = User.objects.get(username = user_username).pk
        rpg = Role_User.objects.filter(id_user_FK=id_user)
        rps = []
        for rp in rpg:
            rps.append(repr(Role.objects.filter(id_role = rp.id_role_FK.id_role).only('name_role')))
        roles = Role.objects.all()
        return render(request, 'AssignRoles.html', {"roles": roles, "rps": rps, "user_username": user_username})

def delete_role_user(request, user_username):
    ru = get_object_or_404(UserRoleForm, username=user_username)
    if request.method == 'POST':
        ru.delete()
        return redirect('assignPermission')