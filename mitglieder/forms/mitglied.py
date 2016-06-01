import datetime
from django import forms
from mitglieder.models import Mitglied

class MitgliederForm(forms.ModelForm):

    vorname = forms.CharField(widget = forms.widgets.TextInput, label = "Vorname")
    nachname = forms.CharField(widget = forms.widgets.TextInput,label = "Nachname")
    anschrift = forms.CharField(widget = forms.widgets.TextInput, label ="Anschrift")
    plz = forms.CharField(widget = forms.widgets.TextInput, label= "PLZ/Ort")
    geburtsdatum = forms.DateField(widget = forms.widgets.DateInput(format='%Y-%m-%d'), label="Geburtsdatum", initial=datetime.datetime.now().date(), input_formats=['%Y-%m-%d'])
    telefon = forms.CharField(widget = forms.widgets.TextInput, label = "Telefon", required = False)
    mobil = forms.CharField(widget = forms.widgets.TextInput, label = "Mobil", required = False)
    email = forms.CharField(widget = forms.widgets.TextInput, label = "Email", required = False)
    iban = forms.CharField(widget = forms.widgets.TextInput, label = "IBAN", required = False)
    bic = forms.CharField(widget = forms.widgets.TextInput, label = "Bic", required = False)
    bank = forms.CharField(widget = forms.widgets.TextInput, label = "Bank", required = False)
    kontoinhaber = forms.CharField(widget = forms.widgets.TextInput, label = "Kontoinhaber", required = False)
    lastschrift = forms.BooleanField(widget=forms.CheckboxInput, label='Lastschrift aktiv', required=False)
    barzahler = forms.BooleanField(widget=forms.CheckboxInput, label='Barzahler',required=False)
    betrag = forms.FloatField(label="Betrag", initial=20)
    new_sepa = forms.BooleanField(widget=forms.CheckboxInput, label='Korrekter Antrag', required=False)


    class Meta:
        model = Mitglied
        fields = [ 'vorname', 'nachname', 'anschrift', 'plz', 'geburtsdatum',
                'telefon', 'mobil', 'email', 'iban', 'bic', 'bank',
                'kontoinhaber', 'lastschrift', 'betrag', 'barzahler', 'new_sepa']

    def save(self, commit=True):
        mitglied = super(MitgliederForm, self).save(commit=False)

        if not self.cleaned_data['kontoinhaber']:
            mitglied.kontoinhaber = u'{0} {1}'.format(self.cleaned_data['vorname'], self.cleaned_data['nachname'])

        if commit:
            mitglied.save()
        return mitglied
