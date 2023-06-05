from django.shortcuts import get_object_or_404, render, redirect
from Autenticacion.forms import RoleForm
from Autenticacion.models import Role

def create_role(request):
    if request.method == "GET":
        return render(request, 'create_role.html', {"form": RoleForm})
    else:
        try:
            form = RoleForm(request.POST)
            new_role = form.save(commit=False)
            new_role.save()
            return redirect('roles')
        except ValueError:
            return render(request, 'create_role.html', {"form": RoleForm, "error": "Error creating role."})
        
def view_roles(request):
    roles = Role.objects.all()
    return render(request, 'roles.html', {"roles": roles})

def delete_role(request, role_id):
    role = get_object_or_404(Role, pk=role_id)
    if request.method == 'POST':
        role.delete()
        return redirect('roles')
    
def role_detail(request, role_id):
    if request.method == 'GET':
        role = get_object_or_404(Role, pk=role_id)
        form = RoleForm(instance=role)
        return render(request, 'role_detail.html', {'role': role, 'form': form})
    else:
        try:
            role = get_object_or_404(Role, pk=role_id)
            form = RoleForm(request.POST, instance=role)
            form.save()
            return redirect('roles')
        except ValueError:
            return render(request, 'role_detail.html', {'role': role, 'form': form, 'error': 'Error updating role.'})

