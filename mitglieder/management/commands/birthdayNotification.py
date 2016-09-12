# -*- coding: utf-8 -*-
from datetime import date, timedelta
from django.core.management.base import BaseCommand, CommandError

from mitglieder.models import Mitglieder
from mitglieder.tools import sendMail

class Command(BaseCommand):

    def __init__(self):
        # To prevent:
        # AttributeError: Command object has no attribute
        super(Command, self).__init__()

    def calculate_age(self, born):
        today = date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    def handle(self, *args, **options):
        allMitglieder = Mitglieder.objects.all()

        # day after tomorrow
        overmorrow = date.today()+timedelta(3)

        birthdayList = []
        for entry in allMitglieder:
            if entry.geburtsdatum.day == overmorrow.day and entry.geburtsdatum.month == overmorrow.month:
                birthdayString = '{0} {1} ({4}) wird am {2}. {3} Jahre alt.'.format(entry.vorname.encode('utf-8', 'strict'), entry.nachname.encode('utf-8', 'strict'), entry.geburtsdatum.strftime("%d.%m"), self.calculate_age(entry.geburtsdatum) + 1, entry.geburtsdatum.strftime("%d.%m.%Y"))

                if entry.email:
                    birthdayString += ' Email: {0}'.format(entry.email)

                if entry.mobil: 
                    birthdayString += ' Tel: {0}'.format(entry.mobil)
                else:
                    if entry.telefon:
                        birthdayString += ' Tel: {0}'.format(entry.telefon)

                birthdayList.append(birthdayString)


        if birthdayList:
            notify = sendMail()
            notify.send(birthdayList, '{0}'.format(overmorrow.strftime("%d.%m.%Y")))
