#!/usr/bin/python
from __future__ import print_function
import sqlite3
import os
import sys

home = os.path.expanduser("~")

conn = sqlite3.connect(os.path.join(home, 'Git/VideoManagement', 'home-video.db'))
c = conn.cursor()

mydir = os.path.join(home, 'Sites/metadata/ts')

for i in os.listdir(mydir):
    s_filename, ext = os.path.splitext(i)
    sid_sql = 'select source_id from source_videos where s_filename = ?'
    c.execute(sid_sql, ('%s.mov' % s_filename,))
    source_id = c.fetchone()[0]
    with open(os.path.join(mydir, i), 'r') as t:
        try:
            pad = '%03d' % 0
            insert_sql = 'insert into source_scenes (source_id, scene_ts, scene_image) values (?, ?, ?)'
            c.execute(insert_sql, (source_id, 0, '%s-%s.png' % (s_filename, pad)))
            for idx, s in enumerate(t, start = 1):
                pad = '%03d' % idx
                scene_image = '%s-%s.png' % (s_filename, pad)
                ts = s.rstrip('\n')
                insert_sql = 'insert into source_scenes (source_id, scene_ts, scene_image) values (?, ?, ?)'
                c.execute(insert_sql, (source_id, ts, scene_image))
        except ValueError as error:
            raise

conn.commit()
conn.close()
