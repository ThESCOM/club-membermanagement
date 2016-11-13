# -*- coding: utf-8 -*-
import kontocheck
from schwifty import IBAN
from schwifty import BIC
from django.core.management.base import BaseCommand, CommandError

from mitglieder.models import Mitglieder

class Command(BaseCommand):

    def __init__(self):
        # To prevent:
        # AttributeError: Command object has no attribute
        super(Command, self).__init__()
        kontocheck.lut_load()

    def handle(self, *args, **options):
        allMitglieder = Mitglieder.objects.all()

        for entry in allMitglieder:
            if entry.new_sepa and not entry.barzahler:

                try:
                    iban = IBAN(entry.iban)
                    actual_bic = entry.bic
                
                    bic = iban.bic
                    try:
                        actual_bank = entry.bank
                        bank = kontocheck.scl_get_bankname(bic.compact)
                        if actual_bank != bank.title():
                            entry.bank = bank.title()
                            entry.save()
                    except Exception as e:
                        pass

                    if actual_bic != bic.compact:
                        entry.bic = bic.compact
                        entry.save()
                        print '{0} {1} {2} {3}'.format(entry.nachname.encode('utf-8', 'strict'), entry.vorname.encode('utf-8', 'strict'),actual_bic, bic.compact)
                except Exception as e:
                    print '##########################################################'
                    print '{0}'.format(e)
                    print '{0} {1} {2} {3}'.format(entry.nachname.encode('utf-8', 'strict'), entry.vorname.encode('utf-8', 'strict'), entry.iban, entry.bic)

