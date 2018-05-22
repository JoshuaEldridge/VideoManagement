#!/usr/bin/python
from __future__ import print_function
import mysql.connector
from mysql.connector import errorcode
import os
import sys
import dbconfig

home = os.path.expanduser("~")

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

mydir = os.path.join(home, 'Sites/metadata/ts')

for i in os.listdir(mydir):
    filename, ext = os.path.splitext(i)
    sid_sql = 'select video_id from videos where filename = "%s.mov"' % filename
    c.execute(sid_sql)
    video_id = c.fetchone()[0]

    with open(os.path.join(mydir, i), 'r') as t:
        print("Inserting scenes for: %s.mov" % filename)
        try:
            pad = '%03d' % 0
            insert_sql = 'insert into scenes (video_id, ts, image_name) values (%s, %s, %s)'
            c.execute(insert_sql, (video_id, 0, '%s-%s.png' % (filename, pad)))
            for idx, s in enumerate(t, start = 1):
                pad = '%03d' % idx
                scene_image = '%s-%s.png' % (filename, pad)
                ts = s.rstrip('\n')
                insert_sql = 'insert into scenes (video_id, ts, image_name) values (%s, %s, %s)'
                c.execute(insert_sql, (video_id, ts, scene_image))
        except ValueError as error:
            raise

conn.commit()
conn.close()
