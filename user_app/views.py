from django.shortcuts import render, HttpResponse,redirect
from .models import userModel
from user_role.models import roleTable
import logging
import string
import re
def index(request):
    all_data = userModel.objects.all() #select * FROM demo_user
    role_data = roleTable.objects.all()
    errorMsgDict = {'UserNameError':'', 'emailError':'','passwordError':''}
    valueDict = {'userName':'','email':'','password':'','confirmPassword':''}
    data = {"user_data":all_data,'role_data':role_data,'errorMsgDict':errorMsgDict,'valueDict':valueDict}
    return render(request, 'admin/register.html', data)



    
def user_registration(request):
    logger = logging.getLogger('mylogger')
    uname = request.POST.get('u_name')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    user_email = request.POST.get('user_email')

    user_role = request.POST.get('user_role')
    user_image = request.FILES.get('user_image')
    user_role = request.POST.get('user_role')

    if user_role.isdigit():
        role_id = int(user_role)
        try:
            role = roleTable.objects.get(pk=role_id)
        except roleTable.DoesNotExist:
            role_id = 0  # Set to 0 if the role doesn't exist
    else:
        role_id = 0  # Set to 0 if 'user_role' is not a valid integer

    role = roleTable.objects.get(pk=user_role)
    print('ssss',user_image)
    user_password = request.POST.get('password')
    user_confirmPassword = request.POST.get('confirmPassword')
    
    print(user_password,user_confirmPassword)




    errorMsgDict ={}
    valueDict = {'userName':uname,'email':user_email,'password':user_password,'confirmPassword':user_confirmPassword}
    userNameVal = userNameValidation(uname)
    firstNameVal = firstNameValidation(first_name)
    lastNameVal = lastNameValidation(last_name)
    emailVal = emailValidation(user_email)
    passwordVal = passwordValidation(user_password, user_confirmPassword)
    roleVal = roleValidation(role)
    # loggger.info('user validation => ' + str())
    if( not( userNameVal['value'])):
        errorMsgDict['userNameError'] = userNameVal['msg']
        print(errorMsgDict['userNameError'])
    if( not( firstNameVal['value'])):
        errorMsgDict['firstNameError'] = firstNameVal['msg']
        print(errorMsgDict['firstNameError'])
    if( not( lastNameVal['value'])):
        errorMsgDict['lastNameError'] = firstNameVal['msg']
        print(errorMsgDict['lastNameError'])
    
    if(not(emailVal['value'])):
        errorMsgDict['emailError'] = emailVal['msg']
        print(errorMsgDict['emailError'])
    if(not(passwordVal)):
        errorMsgDict['passwordError'] = passwordVal['msg']
        print(errorMsgDict['passwordError'])
        print(passwordVal['msg'])
    if(not(roleVal or roleVal==0)):
        errorMsgDict['roleError'] = roleVal['msg']
        print(errorMsgDict['roleError'])
        print(roleVal['msg'])
        # role_data = roleTable.objects.all()
        # data = {'user_data':[],'role_data':role_data,'errorMsgDict':errorMsgDict}
        # return render(request, 'admin/register.html', data)

    if(len(errorMsgDict)>0):
        role_data = roleTable.objects.all()
        return render(request,'admin/register.html',{'value':valueDict,'errorMsg':errorMsgDict,'role_data':role_data})
    user_obj = userModel()
    user_obj.uname = uname
    user_obj.user_first_name = first_name
    user_obj.user_last_name = last_name
    user_obj.user_email = user_email
    user_obj.user_roleID = role
    user_obj.user_profile_pic = user_image
    user_obj.password = user_password
    user_obj.save()
    return redirect('user_index')


def userNameValidation(uname):
        if(not uname):
            return {'value':False, 'msg':"User name can't be empty"}
        if(len(uname)<3):
            return {'value':False,'msg':'User name should contain at least 3 characters'}
        return {'value':True, 'msg':''}
def firstNameValidation(first_name):
        if(not first_name):
            return {'value':False, 'msg':"User first name can't be empty"}
        return {'value':True, 'msg':''}
def lastNameValidation(last_name):
        if(not last_name):
            return {'value':False, 'msg':"User last name can't be empty"}
        return {'value':True, 'msg':''}
def roleValidation(role):
        
        if(not role or not isinstance(role, int) ):
            return {'value':False, 'msg':"User role can't be empty"}
        return {'value':True, 'msg':''}

def emailValidation(email):
        if(not email):
            return {'value':False,'msg':'email address can\'t be empty'}
        if(bool(re.search("^[\w\-\.]+@([\w-]+\.)+[\w-]{2,4}$",email))):
            return {'value':True,'msg':''}
        return {'value': False, 'msg':'email address must be valid'}
def passwordValidation(password,confirmPassword):
        if ( not password):
            return {'value': False, 'msg':'password can\'t be empty'}
        if ( not confirmPassword):
            return {'value': False, 'msg':'confirm password can\'t be empty'}
        if(password!=confirmPassword):
            return {'value': False, 'msg':'password and confirm password must be same'}
        elif(len(password)<8):
            return{'value':False,'msg':'password must contain at least 8 digits'}
        else:
            capitalLetterRange = string.ascii_uppercase #'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            numberRange = string.digits
            letterRange = string.ascii_letters
            if(not(any(x in capitalLetterRange for x in password))):
                return {'value':False, 'msg':'Password must contain at least one capital letter'}
            if (not(any(x in numberRange for x in password))):
                return {'value':False, 'msg':'Password must contain at least one capital letter'}
            if (not(any(x in letterRange and x in numberRange) for x in password)):
                return {'value':False, 'msg':'Password must contain at least one capital letter'}
        return{'value':True,'msg':''}
            







    
    
