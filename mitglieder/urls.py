from django.conf.urls import url
from django.views.generic import RedirectView
import mitglieder.views

urlpatterns = [
        url(r'^login/', RedirectView.as_view(url='/')),
        url(r'^list/$', mitglieder.views.mitgliederList),
        url(r'^addMitglied/$', mitglieder.views.addMitglieder),
        url(r'^editMitglied/(?P<num>[0-9]+)$', mitglieder.views.editMitglieder),
        url(r'^getBankData/(?P<num>[0-9]+)$', mitglieder.views.getBankData),
        url(r'^deleteMitglied/(?P<num>[0-9]+)$', mitglieder.views.deleteMitglieder),
]

