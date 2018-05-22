#!/usr/bin/python
# pip install mysql-connector-python

from __future__ import print_function
import mysql.connector
from mysql.connector import errorcode
import dbconfig
import os
import sys
import json

home = os.path.expanduser("~")
mydir = os.path.join(home, 'Sites/metadata/')
filename = os.path.join(home, 'Git/VideoManagement', 'file-list.txt')
camera_name = "Canon GL1"

try:
    conn = mysql.connector.connect( **dbconfig.mysql )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)

c = conn.cursor()

    
with open(filename) as f:
    content = f.read().splitlines()

for i in content:
    filename, ext = os.path.splitext(i)
    with open(os.path.join(mydir, 'md5', '%s.md5' % filename), 'r') as m, open(os.path.join(mydir,  'json', '%s.json' % filename), 'r') as j:
        md5_hash = m.read()
        try:
            print("Opening: %s.json" % filename)
            js = json.load(j)
            for stream in js["streams"]:
                if stream["codec_type"] == "video":
                    codec_name = stream["codec_name"]
                    codec_long = stream["codec_long_name"]
                    codec_type = stream["codec_type"]
                    codec_tag_string = stream["codec_tag_string"]
                    codec_tag = stream["codec_tag"]
                    width = stream["width"]
                    height = stream["height"]
                    timecode = stream["tags"]["timecode"]
                    creation_time = stream["tags"]["creation_time"]
                    break
            format = js["format"]["format_name"]
            format_long = js["format"]["format_long_name"]
            duration = js["format"]["duration"]
            size = js["format"]["size"]
            bit_rate = js["format"]["bit_rate"]

            sql = '''insert into videos (md5,
                         filename,
                         codec_name,
                         codec_long,
                         codec_type,
                         codec_tag,
                         codec_tag_string,
                         width,
                         height,
                         format,
                         format_long,
                         duration,
                         size,
                         bit_rate,
                         timecode,
                         creation_time,
                         camera_name)
                                values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''

            print('Inserting video: %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s' % (md5_hash, filename, codec_name, codec_long, codec_type, codec_tag, codec_tag_string, width, height, format, format_long, duration, size, bit_rate, timecode, creation_time, camera_name))
            c.execute(sql, (md5_hash, '%s.mov' % filename, codec_name, codec_long, codec_type, codec_tag, codec_tag_string, width, height, format, format_long, duration, size, bit_rate, timecode, creation_time[:-8], camera_name))
        except ValueError as error:
            raise

conn.commit()
conn.close()
