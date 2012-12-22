#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from modules.wxgui import main
from modules.playlist import Playlist
import sys

'''
Created on 22.12.2011

@author: maksim

Creating IPTV playlist from EXCEL Servise PLAN.
'''

if __name__ == '__main__':

    if sys.argv[2] == 'kh' or sys.argv[2] == 'pt':
        soc_start = 7
        soc_end = 56
        base_start = 59
        base_end = 78
        full_start = 81
        full_end = 110
    if sys.argv[2] == 'dn':
        soc_start = 7
        soc_end = 41
        base_start = 44
        base_end = 67
        full_start = 67
        full_end = 66  # in Playlist "items_full = list(range(full_start, full_end + 1))", so result list should be empty

    playlist = Playlist(sys.argv[1], soc_start, soc_end, base_start, base_end, full_start, full_end)
    playlist.parse_xls()
    playlist.save_playlist('tmp/tmp_file.txt')
