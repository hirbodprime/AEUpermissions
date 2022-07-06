from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse , Http404
from django.contrib.auth.models import Group , Permission, User

# all permissions
permissionE = Permission.objects.get(codename='add_expert')
permissionE1 = Permission.objects.get(codename='delete_expert')
permissionE2 = Permission.objects.get(codename='change_expert')
permissionE3 = Permission.objects.get(codename='view_expert')
permissionU = Permission.objects.get(codename='add_users')
permissionU1 = Permission.objects.get(codename='delete_users')
permissionU2 = Permission.objects.get(codename='change_users')
permissionU3 = Permission.objects.get(codename='view_users')

admin_permissions = [
    permissionE , permissionE1 , permissionE2 , permissionE3 ,
    permissionU , permissionU1 , permissionU2 , permissionU3 ,
]

expert_permissions = [
    permissionU , permissionU1 , permissionU2 , permissionU3 ,
]
@login_required(login_url='/admin/')
def create_groups(req):
    admin_group , created = Group.objects.get_or_create(name='admin-group')
    expert_group , created = Group.objects.get_or_create(name='expert-group')
    # user_group = Group.objects.create(name='user-group')
    return HttpResponse("done!")

@login_required(login_url='/admin/')
def add_permissions(req):
    try:
        admin_group = Group.objects.get(name='admin-group')
        expert_group = Group.objects.get(name='expert-group')
        admin_group.permissions.set(admin_permissions)
        expert_group.permissions.set(expert_permissions)
        return HttpResponse("Permissions Added")
    except Group.DoesNotExist:
        raise Http404


def remove_permissions(req):
    try:
        admin_group = Group.objects.get(name='admin-group')
        expert_group = Group.objects.get(name='expert-group')
        admin_group.permissions.clear()
        expert_group.permissions.clear()
        return HttpResponse("Permissions Removed")
    except Group.DoesNotExist:
        raise Http404

