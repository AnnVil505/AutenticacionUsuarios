from django.shortcuts import get_object_or_404, render, redirect
from Autenticacion.models import Role_Permission, Permission, Role

def assign_permission(request, role_id, permission_id):
    if request.method == 'POST':
        arp = Role_Permission(id_role_FK= Role.objects.get(id_role=role_id), id_permission_FK=Permission.objects.get(id_permission=permission_id))
        arp.save()
        return redirect('roles')
    
def delete_role_permission(request, role_id, permission_id):
    if request.method == 'DELETE':
        rp = Role_Permission(id_role_FK= Role.objects.get(id_role=role_id), id_permission_FK=Permission.objects.get(id_permission=permission_id))
        rp.delete()
        return redirect('delete_role_permission')

def view_role_permission(request, role_id):
    if request.method == 'POST':
        rpg = Role_Permission.objects.filter(id_role_FK=role_id)
        rps = []
        for rp in rpg:
            rps.append(repr(Permission.objects.filter(id_permission = rp.id_permission_FK.id_permission).only('name_permission')))
        permissions = Permission.objects.all()
        return render(request, 'AssignPermissions.html', {"permissions": permissions, "rps": rps, "role_id": role_id})