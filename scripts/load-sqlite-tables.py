#!/usr/bin/python
from __future__ import print_function
import sqlite3
import os
import sys
import json


home = os.path.expanduser("~")

conn = sqlite3.connect(os.path.join(home, 'Git/VideoManagement/front-end', 'home-video.db'))

mydir = os.path.join(home, 'Sites/metadata/')

filename = os.path.join(home, 'Git/VideoManagement', 'file-list.txt')
    
with open(filename) as f:
    content = f.read().splitlines()

for i in content:
    base, ext = os.path.splitext(i)
    with open(os.path.join(mydir, 'md5', '%s.md5' % base), 'r') as m, open(os.path.join(mydir,  'json', '%s.json' % base), 'r') as j:
        md5 = m.read()
        try:
            print("Opening: %s.json" % base)
            js = json.load(j)
            for stream in js["streams"]:
                if stream["codec_type"] == "video":
                    codec_name = stream["codec_name"]
                    video_width = stream["width"]
                    video_height = stream["height"]
            duration = js["format"]["duration"]
            sql = '''insert into videos (video_md5, video_filename, video_length, video_format, video_width, video_height) values (?, ?, ?, ?, ?, ?)'''
            c = conn.cursor()
            print('%s %s %s %s %s %s' % (md5, base, duration, codec_name, video_width, video_height))
            c.execute(sql, (md5, '%s.mov' % base, duration, codec_name, video_width, video_height))
        except ValueError as error:
            raise

conn.commit()
conn.close()