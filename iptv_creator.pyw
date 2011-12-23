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
    playlist = Playlist(sys.argv[1])
    playlist.parse_xls()
    playlist.save_playlist('tmp/tmp_file.txt')