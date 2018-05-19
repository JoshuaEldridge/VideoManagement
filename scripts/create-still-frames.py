#!/usr/bin/python
# Just create still frames
# All of the other metadata exists for this scripts

import subprocess
import os
import sys
import argparse
import json

from helper_functions import *

parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbose', default=True)
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-f', '--filename', help='name of the video file. example: 20111022144212.mov')
group.add_argument('-d', '--dir',  help='path to a directory. example: /Volumes/2TB-WD-Elements/DV Library Backup/')
group.add_argument('-l', '--list',  help='list of files to process. example: files-to-process.txt')

args = parser.parse_args()

home = os.path.expanduser("~")

# FFMPEG Settings
poster_scale='627:480'
thumb_scale='314:240'
clip_duration=1
clip_start=5
clip_offset=1

video_directory = None
files_list = None
video_file = None
file_basename = None

# Check that the file or folder is actually valid and readable/writable.
if args.dir is not None:
    if os.path.isdir(args.dir) and os.access(args.dir, os.W_OK):
        video_directory = args.dir
        files_list = find_my_files(video_directory)
    else:
        sys.exit('Error: Directory is not valid or is not writable!')

if args.filename is not None:
    if os.path.isfile(args.filename) and os.access(args.filename, os.R_OK):
        video_file = args.filename
    else:
            sys.exit('Error: File is not valid or not readable!')

if args.list is not None:
    if os.path.isfile(args.list) and os.access(video_file, os.R_OK):
        with open(args.list, 'r') as f:
            files_list = [line.rstrip() for line in f]
    else:
            sys.exit('Error: File is not valid or not readable!')

# Next check that all libraries are available and installed (ffmpeg, ffprobe)
# and the the file and folder permissions are valid - need to write back
if check_lib('ffmpeg') and check_lib('ffprobe') is None:
    sys.exit('Error: This script requires ffmpeg and ffprobe libraries be available in the $PATH!')

# This is the process for a single file:
if video_file is not None:
    file_parts = clean_path(video_file)
    video_duration = read_json_duration(file_parts)
    if os.path.getsize('%s.ts' % file_parts['subfile']) > 0:
        with open('%s.ts' % file_parts['subfile'], 'r') as f:
            for idx, timestamp in enumerate(f, start = 1):
                timestamp = float(timestamp) + float(0.2)
                if idx == 1:

                    create_thumbs(file_parts, clip_scale = poster_scale, mode="still", timestamp = clip_start, part = 0)
                    create_thumbs(file_parts, clip_scale = thumb_scale, mode="still", timestamp = timestamp, part = idx)

                else:
                    create_thumbs(file_parts, clip_scale = thumb_scale, mode="still", timestamp = timestamp, part = idx)
    else:
        create_thumbs(file_parts, clip_scale = poster_scale, mode="still", timestamp = clip_start, part = 0)

else:
    for video_file in files_list:
        file_parts = clean_path(video_file)
        video_duration = read_json_duration(file_parts)
        if os.path.getsize('%s.ts' % file_parts['subfile']) > 0:
            with open('%s.ts' % file_parts['subfile'], 'r') as f:
                for idx, timestamp in enumerate(f, start = 1):
                    timestamp = float(timestamp) + float(0.2)
                    if idx == 1:

                        create_thumbs(file_parts, clip_scale = poster_scale, mode="still", timestamp = clip_start, part = 0)
                        create_thumbs(file_parts, clip_scale = thumb_scale, mode="still", timestamp = timestamp, part = idx)

                    else:
                        create_thumbs(file_parts, clip_scale = thumb_scale, mode="still", timestamp = timestamp, part = idx)
        else:
            create_thumbs(file_parts, clip_scale = poster_scale, mode="still", timestamp = clip_start, part = 0)
