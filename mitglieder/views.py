# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.conf import settings

from mitglieder.models import Mitglied
from mitglieder.forms import MitgliederForm

def main(request):
    print 'XXXXXXXXXXXXx {0}'.format(request.LANGUAGE_CODE)
    return render(request, 'index.html', { "TITLE": settings.VEREINSNAME})

@login_required
def mitgliederList(request):
    allObjects = Mitglied.objects.all()

    return render(request, "list.html", {"TITLE": settings.VEREINSNAME, "mitgliederList": allObjects})

@login_required
def getBankData(request, num):
    mitglied = Mitglied.objects.get(id=int(num))

    return render(request, "bankList.html", {"TITLE": settings.VEREINSNAME, "mitglied": mitglied})

@login_required
def editMitglieder(request, num):

    mitgliedInstance = Mitglied.objects.get(id=int(num))

    mitgliedForm = MitgliederForm(request.POST or None, instance=mitgliedInstance)

    if mitgliedForm.is_valid():
        mitgliedForm.save()

        return redirect('/mitglieder/list/')
    return render_to_response('editMitglieder.html', {"TITLE": settings.VEREINSNAME, 'mitgliederForm': mitgliedForm, "ID": num }, context_instance=RequestContext(request))

@login_required
def addMitglieder(request):

    if request.method == 'POST':
        mitgliederForm = MitgliederForm(data = request.POST)

        if mitgliederForm.is_valid():
            mitglieder = mitgliederForm.save()
            return redirect('/mitglieder/list/')
    else:
        mitgliederForm = MitgliederForm()

    return render_to_response('addMitglieder.html', {"TITLE": settings.VEREINSNAME, 'mitgliederForm': mitgliederForm }, context_instance=RequestContext(request))

@login_required
def deleteMitglieder(request, num):

    if num:
        mitglieder = Mitglied.objects.get(id=int(num))
        if mitglieder:
            mitglieder.delete()
    return redirect('/mitglieder/list/')

