import datetime
from django import forms
from django.utils.translation import ugettext_lazy as _
from mitglieder.models import Mitglied, BETRAG
import datetime

class MitgliederForm(forms.ModelForm):

    vorname = forms.CharField(widget = forms.widgets.TextInput, label = _("Vorname"))
    nachname = forms.CharField(widget = forms.widgets.TextInput,label = _("Nachname"))
    anschrift = forms.CharField(widget = forms.widgets.TextInput, label =_("Anschrift"))
    plz = forms.CharField(widget = forms.widgets.TextInput, label= _("PLZ/Ort"))
    geburtsdatum = forms.DateField(widget = forms.widgets.DateInput(format='%Y-%m-%d'), label=_("Geburtsdatum"), initial=datetime.datetime.now().date(), input_formats=['%Y-%m-%d'])
    telefon = forms.CharField(widget = forms.widgets.TextInput, label = _("Telefon"), required = False)
    mobil = forms.CharField(widget = forms.widgets.TextInput, label = _("Mobil"), required = False)
    email = forms.CharField(widget = forms.widgets.TextInput, label = _("Email"), required = False)
    iban = forms.CharField(widget = forms.widgets.TextInput, label = _("IBAN"), required = False)
    bic = forms.CharField(widget = forms.widgets.TextInput, label = _("Bic"), required = False)
    bank = forms.CharField(widget = forms.widgets.TextInput, label = _("Bank"), required = False)
    kontoinhaber = forms.CharField(widget = forms.widgets.TextInput, label = _("Kontoinhaber"), required = False)
    lastschrift = forms.BooleanField(widget=forms.CheckboxInput, label=_('Lastschrift aktiv'), required=False)
    barzahler = forms.BooleanField(widget=forms.CheckboxInput, label=_('Barzahler'),required=False)
    betrag = forms.CharField(widget=forms.Select(choices=BETRAG),label=_("Betrag"))
    mandatsreferenz = forms.CharField(widget=forms.widgets.TextInput, label=_("Mandatsreferenz (ID_Datum)"), required=False)
    mailverteiler = forms.BooleanField(widget=forms.CheckboxInput, label=_('Mailverteiler Mitglied'), required=False)


    class Meta:
        model = Mitglied
        fields = [ 'vorname', 'nachname', 'anschrift', 'plz', 'geburtsdatum',
                'telefon', 'mobil', 'email', 'iban', 'bic', 'bank',
                'kontoinhaber', 'lastschrift', 'betrag', 'barzahler',
                'mandatsreferenz', 'mailverteiler']

    def save(self, commit=True):
        mitglied = super(MitgliederForm, self).save(commit=False)

        if not self.cleaned_data['kontoinhaber']:
            mitglied.kontoinhaber = u'{0} {1}'.format(self.cleaned_data['vorname'], self.cleaned_data['nachname'])

        # if no email exists, he can not be part of a mailverteiler
        if not self.cleaned_data['email']:
            mitglied.mailverteiler = False

        if not self.cleaned_data['mandatsreferenz']:
            mitgliedID = 0
            for entry in Mitglieder.objects.all():
                if entry.id > mitgliedID:
                    mitgliedID = entry.id

            mitgliedID += 1

            if mitglied.id:
                mitgliedID = mitglied.id

            mitglied.mandatsreferenz = '{0}{1}'.format(mitgliedID, datetime.date.today().strftime("%d%m%Y"))

        if commit:
            mitglied.save()
        return mitglied
