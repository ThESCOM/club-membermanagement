from django.conf.urls import url
import userAccounts.views

urlpatterns = [
        url(r'^login/$', userAccounts.views.login, name='login'),
        url(r'^list/$', userAccounts.views.userList),
        url(r'^addUser$', userAccounts.views.addUser),
        #url(r'^editMitglied/(?P<num>[0-9]+)$', mitglieder.views.editMitglieder),
        #url(r'^getBankData/(?P<num>[0-9]+)$', mitglieder.views.getBankData),
        #url(r'^deleteMitglied/(?P<num>[0-9]+)$', mitglieder.views.deleteMitglieder),
]

