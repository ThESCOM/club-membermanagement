# -*- coding: utf-8 -*-
import smtplib

class sendMail():
    def createhtmlmail(self, SUBJECT, mitgliederList):
        from email.mime.text import MIMEText
        import mimetools
        import cStringIO

        message = '{0}'.format('Folgende Mitglieder haben demnaechst Geburtstag: \n'.decode().encode('utf8', 'strict'))
        for item in mitgliederList:
            message += '- ' + str(item) + '\n'

        out = cStringIO.StringIO()
        txtin = cStringIO.StringIO(message)
        writer = MIMEText(message)

        writer['Subject'] = SUBJECT
        writer['MIME-Version'] = '1.0'
        writer['From'] = 'EMAIL'
        writer['To'] = 'EMAIL'

        txtin.close()

        return writer.as_string()

    def send(self, mitgliederList, datestring):
        FROM = 'EMAIL'
        TO = [ 'EMAIL' ]
        SUBJECT = 'Geburtstagserinnerung fuer {0}'.format(datestring)

        message = self.createhtmlmail(SUBJECT, mitgliederList)

        server = smtplib.SMTP('SMTP-HOST')
        server.sendmail(FROM, TO, message)
        server.quit()
