#!/usr/bin/python
import sqlite3
import os

home = os.path.expanduser("~")
conn = sqlite3.connect(os.path.join(home, 'Git/VideoManagement', 'home-video.db'))

c = conn.cursor()

c.execute('''CREATE TABLE videos
                (video_md5 text, video_filename text, video_length real, video_scenes integer, video_format text, video_width integer, video_height integer)''')

conn.commit()

conn.close()