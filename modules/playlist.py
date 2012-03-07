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


    def __init__(self, open_file, soc_start = 7, soc_end = 56, base_start = 59, base_end = 78, full_start = 81, full_end = 110):
        '''
        Constructor
        '''
        self.sheet0 = open_workbook(open_file).sheet_by_index(0)
        self.social = list(range(int(soc_start), int(soc_end) + 1))
        self.base = list(range(int(base_start), int(base_end) + 1))
        self.full = list(range(int(full_start), int(full_end) + 1))
        
    def save_playlist(self, path):
        
        f = codecs.open(path, "w", "utf-8")
        f.write(self.playlist)
        f.close()
        print(self.playlist)
        print('Плейлист успешно сохранен в файл tmp/tmp.txt.\n')
              
        
    def parse_xls(self):
        self.playlist = '#EXTM3U\n\n'
        items_social = []
        items_base = []
        items_full = []

        [items_social.append(i) for i in self.social]
        [items_base.append(i) for i in self.base]
        [items_full.append(i) for i in self.full]

        for i in items_social:
            item = self.sheet0.row_values(i-1, 0, 3)
            if item[1] < 10:
                self.playlist += '#EXTINF:0,00'
            elif item[1] > 99:
                self.playlist += '#EXTINF:0,'
            else:
                self.playlist += '#EXTINF:0,0'
            self.playlist += str(item[1]) + ' ' + '[' + 'SOCIAL' + ']' + ' ' + item[0] + '\n' + 'udp://@' + str(item[2]) + ':5004' + '\n\n'
        for i in items_base:
            item = self.sheet0.row_values(i-1, 0, 3)
            if item[1] < 10:
                self.playlist += '#EXTINF:0,00'
            elif item[1] > 99:
                self.playlist += '#EXTINF:0,'
            else:
                self.playlist += '#EXTINF:0,0'
            self.playlist += str(item[1]) + ' ' + '[' + 'BASE' + ']' + ' ' + item[0] + '\n' + 'udp://@' + str(item[2]) + ':5004' + '\n\n'
        for i in items_full:
            item = self.sheet0.row_values(i-1, 0, 3)
            if item[1] < 10:
                self.playlist += '#EXTINF:0,00'
            elif item[1] > 99:
                self.playlist += '#EXTINF:0,'
            else:
                self.playlist += '#EXTINF:0,0'
            self.playlist += str(item[1]) + ' ' + '[' + 'FULL' + ']' + ' ' + item[0] + '\n' + 'udp://@' + str(item[2]) + ':5004' + '\n\n'
