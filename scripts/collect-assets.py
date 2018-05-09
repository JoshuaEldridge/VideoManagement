#!/usr/bin/python

# This script should try to aggregate the directories
# created by the archive-video-scenes.py script

import os
import shutil

source_dir = "/Volumes/2TB-WD-Elements/DV Library Backup"

home = os.path.expanduser("~")

# print os.listdir(source_dir)

f = []
for (dirpath, dirnames, filenames) in os.walk(source_dir):
    print dirpath, dirnames, filenames
    for d in dirnames:
        dir_path = os.path.join(source_dir, d)
        for i in os.listdir(dir_path):
            if os.path.isdir(os.path.join(dir_path, i)):
                source = os.path.join(dir_path, i)
                target = os.path.join(home, 'Git/VideoManagement/video-library/images/', i)
                print source, target
                shutil.copytree(source, target)
    break