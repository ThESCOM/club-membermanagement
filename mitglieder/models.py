from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

BETRAG = (('20', '20'),
          ('100', '100'),
        )

class Mitglied(models.Model):
    vorname = models.CharField(_("Vorname"), blank=False, null=False, max_length=50)
    nachname = models.CharField(_("Nachname"), blank=False, null=False, max_length=50)
    anschrift = models.CharField(_("Anschrift"), blank=False, null=False, max_length=50)
    plz = models.CharField(_("PLZ/Ort"), blank=False, null=False, max_length=50)
    geburtsdatum = models.DateField(_("Geburtsdatum"), blank=False, null=False)
    telefon = models.CharField(_("Telefon"), blank=True, null=True, max_length=50)
    mobil = models.CharField(_("Mobil"), blank=True, null=True, max_length=50)
    email = models.CharField(_("Email"), blank=True, null=True, max_length=50)
    iban = models.CharField(_("IBAN"), blank=False, null=False, max_length=50)
    bic = models.CharField(_("Bic"), blank=False, null=False, max_length=50)
    bank = models.CharField(_("Bank"), blank=True, null=True, max_length=50)
    kontoinhaber = models.CharField(_("Kontoinhaber"), blank=True, null=True, max_length=50)
    lastschrift = models.BooleanField(_("Lastschrift aktiv"), default=False)
    barzahler = models.BooleanField(_("Barzahler"), default=False)
    betrag = models.CharField(_("Betrag"), choices=BETRAG, default='20', max_length=5)
    mandatsreferenz = models.CharField(_("Mandatsreferenz"), blank=True, null=True, max_length=200)
    mailverteiler = models.BooleanField(_("Mailverteiler"), default=True)
