#!/usr/bin/python
# Video Archival Process
# 1. Check to see if the video file has already been archived
# 2. Store the MD5 of the video file
# 3. Create still and animated gifs to represent the file
# 4. Export file metadata in JSON

import subprocess
import os
import sys
import argparse
import random
import pickle

from helper_functions import *

parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbose', default=True)
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-f', '--filename', help='name of the video file. example: 20111022144212.mov')
group.add_argument('-d', '--dir',  help='path to a directory. example: /Volumes/2TB-WD-Elements/DV Library Backup/')
group.add_argument('-l', '--list',  help='list of files to process. example: files-to-process.txt')

args = parser.parse_args()

home = os.path.expanduser("~")
hash_cache_file = os.path.join(home, 'Git/VideoManagement/scripts/video_hashes.cache')
debug_mode = False

# FFMPEG Settings
clip_duration=4
clip_fps=15
clip_scale=320

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

# One of the first things we should do is to check the global list of assets
# to see if we even need to process the file. The first step is to look for a local
# version of the cache file. TO DO: Pull the file from a remote location.
if debug_mode:
    hash_set = set()
else:
    hash_set = load_hash_cache(hash_cache_file)

# Create the subdirectory for the resulting GIF files and metadata
# This is the process for a single file:
if video_file is not None:
    file_parts = clean_path(video_file)
    if not os.path.isdir(file_parts['subdir']):
        os.mkdir(file_parts['subdir'])
    md5 = dump_md5(file_parts)

    if md5 not in hash_set:
        video_duration = float(get_video_duration(file_parts).rstrip())
        detect_scenes(file_parts)

        if os.path.getsize('%s.ts' % file_parts['subfile']) > 0:
            part = 1
            with open('%s.ts' % file_parts['subfile'], 'r') as f:
                for timestamp in f:
                    timestamp = float(timestamp.rstrip())
                    if timestamp > (video_duration - clip_duration):
                        timestamp = (video_duration - clip_duration)
                    create_thumbs(file_parts, timestamp = timestamp, clip_duration = clip_duration, clip_fps = clip_fps, clip_scale = clip_scale, part = part)
                    part += 1
        else:
            create_thumbs(file_parts, clip_duration = clip_duration, clip_fps = clip_fps, clip_scale = clip_scale)

        dump_md5(file_parts)
        dump_video_metadata(file_parts)
#         hash_set.add(md5)
    else:
        print "Notice: This video %s was found in the catalog" % file_parts['name']

else:
    for video_file in files_list:
        file_parts = clean_path(video_file)
        if not os.path.isdir(file_parts['subdir']):
            os.mkdir(file_parts['subdir'])
        md5 = dump_md5(file_parts)
        if md5 not in hash_set:
            video_duration = float(get_video_duration(file_parts).rstrip())
            detect_scenes(file_parts)

            if os.path.getsize('%s.ts' % file_parts['subfile']) > 0:
                part = 1
                with open('%s.ts' % file_parts['subfile'], 'r') as f:
                    for timestamp in f:
                        timestamp = float(timestamp.rstrip())
                        create_thumbs(file_parts, timestamp = timestamp, clip_duration = clip_duration, clip_fps = clip_fps, clip_scale = clip_scale, part = part)
                        part += 1
            else:
                create_thumbs(file_parts, clip_duration = clip_duration, clip_fps = clip_fps, clip_scale = clip_scale)

            dump_md5(file_parts)
            dump_video_metadata(file_parts)
            hash_set.add(md5)
        else:
            print "Notice: This video %s was found in the catalog" % file_parts['name']

pickle.dump(hash_set, open(hash_cache_file, "wb"))
