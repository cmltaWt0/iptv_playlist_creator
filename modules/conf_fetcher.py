from ConfigParser import ConfigParser
from datetime import date, timedelta

yesterday = date.today() - timedelta(1)

date_file = yesterday.strftime("%d.%m.%Y")
date_dir = yesterday.strftime("%m.%Y")


def fetcher():
    a = {}
    config = ConfigParser()
    config.read('conf/base.cfg')

    a ['send_from'] = (config.get('from', 'send_from'))
    a ['send_to'] = [config.get('to', 'send_to1'), config.get('to', 'send_to2')]
    a ['send_cc'] = [config.get('to', 'send_cc1'), config.get('to', 'send_cc2')]
    a ['text'] = config.get('text', 'text') + ' '
    a ['files'] = [config.get('file', 'f1') + date_dir + config.get('file', 'f2') + date_file + '.' + config.get('file', 'f_type')]
    a ['subject'] = config.get('subject', 'subject')
    a ['server'] = config.get('smtp_server', 'server')

    return a
