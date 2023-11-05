from django.shortcuts import render, HttpResponse,redirect
from .models import roleTable
def role_index(request):
    all_data = roleTable.objects.all() #select * FROM demo_user
    data = {"role_data":all_data}
    return render(request, 'role/role_register.html', data)

def role_insert(request):
    
    rolename = request.POST.get('user_role')
    rolename = rolename.title()
    if roleTable.objects.filter(roleName=rolename).exists():
        roleError = "Role already exists. Please choose a different role."
        all_data = roleTable.objects.all()
        data = {'role_data':all_data,'roleError':roleError}
        return render(request,'role/role_register.html',data)
    if not rolename:
        roleError = "Role can\'t be empty"
        all_data = roleTable.objects.all()
        data = {'role_data':all_data,'roleError':roleError}
        return render(request,'role/role_register.html',data)
    user_obj = roleTable()
    user_obj.roleName = rolename
    user_obj.save()
    return redirect('role_index')