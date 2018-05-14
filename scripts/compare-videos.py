#!/usr/bin/python
from __future__ import print_function
import sqlite3
import os
import sys

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
    
home = os.path.expanduser("~")

conn = sqlite3.connect(os.path.join(home, 'Git/VideoManagement/video-library', 'home-video.db'))
conn.row_factory = dict_factory

filename = os.path.join(home, 'Git/VideoManagement', 'video_file_hashes.csv')

sql = '''select s_md5, s_filename from source_videos'''
c = conn.cursor()
for row in c.execute(sql):
    print(row)

sql = '''select s_md5 from source_videos'''

known_md5s = set()
for row in c.execute(sql):
    known_md5s.add(row['s_md5'])

print(known_md5s)

with open(filename, 'r') as f:
    contents = f.read().splitlines()
for i in contents:
    pieces = [x.strip() for x in i.split(',')]

    if pieces[0] in known_md5s:
#         print("Found %s in Library" % pieces[0])
        pass
    else:
#         print("%s not Found" % i)
        print(i.split(",")[3])


conn.commit()
conn.close()
