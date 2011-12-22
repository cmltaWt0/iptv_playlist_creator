import ConfigParser

'''
Created on 22.12.2011

@author: maksim
'''

########################################################################

#need to going to module
from datetime import date
from calendar import monthrange

date_ = date.today()

#calculate latest day in last mounth
if date_.day == 1:
    mrange_ = monthrange(date_.year, date_.month - 1)
    date_ = date_.replace(month = date_.month - 1, day = mrange_[1])
    date_file = date_.strftime("%d.%m.%Y")
    date_dir = date_.strftime("%m.%Y")
#calculate yesterday's day
else:
    date_ = date_.replace(day = date_.day -1)
    date_file = date_.strftime("%d.%m.%Y")
    date_dir = date_.strftime("%m.%Y")
########################################################################

def fetcher():
    a = {}
    config = ConfigParser.ConfigParser()
    config.read('conf/base.cfg')

    a ['send_from'] = (config.get('from', 'send_from'))
    a ['send_to'] = [config.get('to', 'send_to1'), config.get('to', 'send_to2')]
    a ['send_cc'] = [config.get('to', 'send_cc1'), config.get('to', 'send_cc2')]
    a ['text'] = config.get('text', 'text') + ' '
    a ['files'] = [config.get('file', 'f1') + date_dir + config.get('file', 'f2') + date_file + '.' + config.get('file', 'f_type')]
    a ['subject'] = config.get('subject', 'subject')
    a ['server'] = config.get('smtp_server', 'server')

    return a