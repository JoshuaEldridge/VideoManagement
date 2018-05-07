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
        dir_path = os.path.join(dirpath, d)
        for i in os.listdir(dir_path):
            if not os.path.isdir(os.path.join(dir_path, i)):
                filename, file_extension = os.path.splitext(os.path.join(dir_path, i))
#                 print filename, file_extension
                if file_extension == '.ts':
                    source = os.path.join(dir_path, i)
                    target = os.path.join(home, 'Sites/metadata/ts/', i)
                    shutil.copyfile(source, target)
#     break