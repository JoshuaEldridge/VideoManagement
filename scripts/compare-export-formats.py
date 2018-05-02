#!/usr/bin/python

# This script should try to aggregate the directories
# created by the archive-video-scenes.py script

import os
import shutil
from helper_functions import *

file = "/Volumes/2TB-WD-Elements/DV Library Backup/Reel 1001/Reel-1001-02.mov"
file_parts = clean_path(file)
for i in ['default', 'compact', 'csv', 'flat', 'ini', 'json', 'xml']:
    dump_video_metadata(file_parts, i)