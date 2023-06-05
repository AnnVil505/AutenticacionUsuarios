from django.shortcuts import get_object_or_404, render, redirect
from Autenticacion.forms import PermissionForm
from Autenticacion.models import Permission

def create_permission(request):
    if request.method == "GET":
        return render(request, 'create_permission.html', {"form": PermissionForm})
    else:
        try:
            form = PermissionForm(request.POST)
            new_permission = form.save(commit=False)
            new_permission.save()
            return redirect('permissions')
        except ValueError:
            return render(request, 'create_permission.html', {"form": PermissionForm, "error": "Error creating permission."})

def view_permission(request):
    permissions = Permission.objects.all()
    return render(request, 'permissions.html', {"permissions": permissions})

def delete_permission(request, permission_id):
    permission = get_object_or_404(Permission, pk=permission_id)
    if request.method == 'POST':
        permission.delete()
        return redirect('permissions')
    
def permission_detail(request, permission_id):
    if request.method == 'GET':
        permission = get_object_or_404(Permission, pk=permission_id)
        form = PermissionForm(instance=permission)
        return render(request, 'permission_detail.html', {'permission': permission, 'form': form})
    else:
        try:
            permission = get_object_or_404(Permission, pk=permission_id)
            form = PermissionForm(request.POST, instance=permission)
            form.save()
            return redirect('permissions')
        except ValueError:
            return render(request, 'permission_detail.html', {'permission': permission, 'form': form, 'error': 'Error updating permission.'})

