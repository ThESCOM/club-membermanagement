from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from django.conf import settings

from django.contrib.auth import login as django_login, authenticate, logout as django_logout

from userAccounts.forms import AuthenticationForm, RegistrationForm
from userAccounts.models import AdminUser
# Create your views here.

def login(request):
    """
    Login views
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(email=request.POST['email'], password=request.POST['password'])
            if user is not None:
                if user.is_active:
                    django_login(request, user)
                    return redirect('/')
    else:
        form = AuthenticationForm()

    return render_to_response('accounts/login.html', {
        "TITLE": settings.VEREINSNAME, 'form': form,
        }, context_instance=RequestContext(request))

@login_required
def logout(request):
    """
    Logout view
    """
    django_logout(request)
    return redirect('/')

@login_required
def userList(request):
    allObjects = AdminUser.objects.all()

    return render(request, "userList.html", {"TITLE": settings.VEREINSNAME, "userList": allObjects})

@login_required
def addUser(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/user/list')
    else:
        form = RegistrationForm()
    return render_to_response('accounts/register.html', { "TITLE": settings.VEREINSNAME, 'form': form }, context_instance=RequestContext(request))
