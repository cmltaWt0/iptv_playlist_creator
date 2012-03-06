# -*- coding: utf-8 -*-
from xlrd import open_workbook
import codecs

'''
Created on 23.12.2011

@author: maksim
'''

class Playlist(object):
    '''
    classdocs
    '''


    def __init__(self, open_file):
        '''
        Constructor
        '''
        self.sheet0 = open_workbook(open_file).sheet_by_index(0)
        
    def save_playlist(self, path):
        
        f = codecs.open(path, "w", "utf-8")
        f.write(self.playlist)
        f.close()
              
        
    def parse_xls(self):
        self.playlist = '#EXTM3U\n\n'
        items = []
        social = list(range(7,57))
        base = list(range(59,79))
        full = list(range(81,111))

        [items.append(i) for i in social]
        [items.append(i) for i in base]
        [items.append(i) for i in full]

        for i in items:
            item = self.sheet0.row_values(i-1, 0, 3)
            if item[1] < 10:
                self.playlist += '#EXTINF:0,00'
            elif item[1] > 99:
                self.playlist += '#EXTINF:0,'
            else:
                self.playlist += '#EXTINF:0,0'
            self.playlist += str(item[1]) + ' ' + '[' + 'SOCIAL' + ']' + ' ' + item[0] + '\n' + 'udp://@' + str(item[2]) + ':5004' + '\n\n'
        
    
