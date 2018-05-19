#!/usr/bin/python
from __future__ import print_function
import os
import sys
import argparse
import sqlite3
from helper_functions import *

parser = argparse.ArgumentParser()

parser.add_argument('-d', '--dir',  help='path to a directory. example: /Volumes/2TB-WD-Elements/DV Library Backup/')
parser.add_argument('-e', '--ext',  help='file extensions to match against. (".jpg", ".gif")')

args = parser.parse_args()

home = os.path.expanduser("~")

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
    
home = os.path.expanduser("~")

if os.path.isdir(args.dir) and os.access(args.dir, os.W_OK):
    files_directory = args.dir
    files_list = find_my_files(files_directory, args.ext)
else:
    sys.exit('Error: Directory is not valid or is not writable!')


for video_file in files_list:
    file_parts = clean_path(video_file)
    md5_digest = md5(file_parts['abs'])
    print(file_parts, md5_digest)

# conn = sqlite3.connect(os.path.join(home, 'Git/VideoManagement/video-library', 'home-video.db'))
# conn.row_factory = dict_factory
# 
# filename = os.path.join(home, 'Git/VideoManagement', 'video_file_hashes.csv')
# 
# sql = '''select s_md5, s_filename from source_videos'''
# c = conn.cursor()
# for row in c.execute(sql):
#     print(row)
# 
# sql = '''select s_md5 from source_videos'''
# 
# known_md5s = set()
# for row in c.execute(sql):
#     known_md5s.add(row['s_md5'])
# 
# print(known_md5s)

# with open(filename, 'r') as f:
#     contents = f.read().splitlines()
# for i in contents:
#     pieces = [x.strip() for x in i.split(',')]
# 
#     if pieces[0] in known_md5s:
#         print("Found %s in Library" % pieces[0])
#     else:
#         print("%s not Found" % i)
# 
# 
# conn.commit()
# conn.close()
