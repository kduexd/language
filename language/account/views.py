from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from account.forms import UserForm, UserProfileForm


def register(request):
    template = 'account/register.html'
    if request.method=='GET':
        return render(request,template,{'userForm':UserForm(),'userProfileForm':UserProfileForm()})
    # request.method == 'POST':
    
    userForm = UserForm(request.POST)
    userProfileForm = UserProfileForm(request.POST)
    if not (userForm.is_valid() and userProfileForm.is_valid()):
        return render(request,template,{'userForm':userForm,'userProfileForm':userProfileForm})
    
    user = userForm.save()
    user.set_password(user.password)
    user.save()
    userProfile = userProfileForm.save(commit=False)
    userProfile.user = user
    userProfile.save()
    messages.success(request, '歡迎註冊')
    return redirect(reverse('main:main'))
    
    # Create your views here.
