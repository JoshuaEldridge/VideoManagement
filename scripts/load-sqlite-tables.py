#!/usr/bin/python
import sqlite3
import os
import json

home = os.path.expanduser("~")

conn = sqlite3.connect(os.path.join(home, 'Git/VideoManagement', 'home-video.db'))

md5_file = '/Volumes/2TB-WD-Elements/DV Library Backup/Reel 1001/Reel-1001-01/Reel-1001-01.md5'
json_file = '/Volumes/2TB-WD-Elements/DV Library Backup/Reel 1001/Reel-1001-01/Reel-1001-01.json'


with open(md5_file, 'r') as f:
    md5 = f.read()

print md5
# with open(json_file) as f:
#     md = json.load(f)
# 
# for i in md['streams']:
#     print i
    
c = conn.cursor()



# c.execute('''insert into videos
#                 (video_md5 text, video_filename text, video_length real video_scenes integer, video_format text, video_width integer, video_height integer)''')
# conn.commit()
conn.close()