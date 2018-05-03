#!/usr/bin/python
import sqlite3
import os
import json

home = os.path.expanduser("~")

conn = sqlite3.connect(os.path.join(home, 'Git/VideoManagement', 'home-video.db'))

mydir = os.path.join(home, 'Sites/metadata/md5/')
md5_file = '/Volumes/2TB-WD-Elements/DV Library Backup/Reel 1001/Reel-1001-01/Reel-1001-01.md5'
json_file = '/Volumes/2TB-WD-Elements/DV Library Backup/Reel 1001/Reel-1001-01/Reel-1001-01.json'

for i in os.listdir(mydir):
    with open(os.path.join(mydir, i), 'r') as f:
        md5 = f.read()
        filename = os.path.basename(i)
        base, ext = os.path.splitext(filename)
        
    sql = '''insert into videos (video_md5, video_filename) values (?, ?)'''
    print '%s.mov' % base
    c = conn.cursor()
    c.execute(sql, (md5, '%s.mov' % base))

conn.commit()
conn.close()