#!/usr/bin/python
from __future__ import print_function
import sqlite3
import os
import sys
from helper_functions import *

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
    
home = os.path.expanduser("~")

conn = sqlite3.connect(os.path.join(home, 'Git/VideoManagement/video-library', 'home-video.db'))
conn.row_factory = dict_factory

# filename = os.path.join(home, 'Git/VideoManagement', 'video_file_hashes.csv')

sql = '''select s_md5, s_filename, s_size from source_videos'''
c = conn.cursor()
for row in c.execute(sql):
    print(row['s_filename'], sizeof_fmt(row['s_size']))

# sql = '''select s_md5 from source_videos'''
# 
# known_md5s = set()
# for row in c.execute(sql):
#     known_md5s.add(row['s_md5'])
# 
# print(known_md5s)
conn.close()
