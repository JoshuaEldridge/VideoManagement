#!/usr/bin/python

# This script should try to aggregate the directories
# created by the archive-video-scenes.py script

import os

source_dir = "/Volumes/2TB-WD-Elements/DV Library Backup"

# print os.listdir(source_dir)

f = []
for (dirpath, dirnames, filenames) in os.walk(source_dir):
#     print dirpath, dirnames, filenames
#     f.extend(filenames)
    for d in dirnames:
        for i in os.listdir(d):
            if os.path.isdir(os.path.join(source_dir, d, i)):
                print os.path.join(source_dir, d, i)
    break