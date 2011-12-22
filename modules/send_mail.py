import smtplib
import os
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders

'''
Created on 22.12.2011

@author: maksim
'''

def send_mail(**a):
    assert type(a['send_to'])==list
    assert type(a['files'])==list

    msg = MIMEMultipart()
    msg['From'] = a['send_from']
    msg['To'] = COMMASPACE.join(a['send_to'])
    msg['cc'] = COMMASPACE.join(a['send_cc'])
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = a['subject']

    msg.attach( MIMEText(a['text']) )


    for f in a['files']:
        part = MIMEBase('application', "octet-stream")
        part.set_payload( open(f,"rb").read() )
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
        msg.attach(part)

    try:
        smtp = smtplib.SMTP(a['server'])
        smtp.sendmail(a['send_from'], a['send_to']+a['send_cc'], msg.as_string())
        smtp.close()
    except Exception.SMTPException:
        pass
