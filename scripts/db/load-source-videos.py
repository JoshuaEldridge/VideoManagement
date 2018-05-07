#!/usr/bin/python
from __future__ import print_function
import sqlite3
import os
import sys
import json

s_camera_name = "Canon GL1"
home = os.path.expanduser("~")

conn = sqlite3.connect(os.path.join(home, 'Git/VideoManagement', 'home-video.db'))

mydir = os.path.join(home, 'Sites/metadata/')

filename = os.path.join(home, 'Git/VideoManagement', 'file-list.txt')
    
with open(filename) as f:
    content = f.read().splitlines()

for i in content:
    s_filename, ext = os.path.splitext(i)
    with open(os.path.join(mydir, 'md5', '%s.md5' % s_filename), 'r') as m, open(os.path.join(mydir,  'json', '%s.json' % s_filename), 'r') as j:
        s_md5 = m.read()
        try:
            print("Opening: %s.json" % s_filename)
            js = json.load(j)
            for stream in js["streams"]:
                if stream["codec_type"] == "video":
                    s_codec_name = stream["codec_name"]
                    s_codec_long = stream["codec_long_name"]
                    s_codec_type = stream["codec_type"]
                    s_codec_tag_string = stream["codec_tag_string"]
                    s_codec_tag = stream["codec_tag"]
                    s_width = stream["width"]
                    s_height = stream["height"]
                    s_timecode = stream["tags"]["timecode"]
                    s_creation_time = stream["tags"]["creation_time"]
                    break
            s_format = js["format"]["format_name"]
            s_format_long = js["format"]["format_long_name"]
            s_duration = js["format"]["duration"]
            s_size = js["format"]["size"]
            s_bit_rate = js["format"]["bit_rate"]

            sql = '''insert into source_videos (s_md5,
                         s_filename,
                         s_codec_name,
                         s_codec_long,
                         s_codec_type,
                         s_codec_tag,
                         s_codec_tag_string,
                         s_width,
                         s_height,
                         s_format,
                         s_format_long,
                         s_duration,
                         s_size,
                         s_bit_rate,
                         s_timecode,
                         s_creation_time,
                         s_camera_name)
                                values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
            c = conn.cursor()
            print('%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s' % (s_md5, s_filename, s_codec_name, s_codec_long, s_codec_type, s_codec_tag, s_codec_tag_string, s_width, s_height, s_format, s_format_long, s_duration, s_size, s_bit_rate, s_timecode, s_creation_time, s_camera_name))
            c.execute(sql, ((s_md5, '%s.mov' % s_filename, s_codec_name, s_codec_long, s_codec_type, s_codec_tag, s_codec_tag_string, s_width, s_height, s_format, s_format_long, s_duration, s_size, s_bit_rate, s_timecode, s_creation_time, s_camera_name)))
        except ValueError as error:
            raise

conn.commit()
conn.close()
