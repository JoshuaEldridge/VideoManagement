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

from helper_functions import *

parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbose', default=True)
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-f', '--filename', help='name of the video file. example: 20111022144212.mov')
group.add_argument('-d', '--dir',  help='path to a directory. example: /Volumes/2TB-WD-Elements/DV Library Backup/')
group.add_argument('-l', '--list',  help='list of files to process. example: files-to-process.txt')

args = parser.parse_args()

hash_cache_file = '/Users/161619/Git/VideoManagement/scripts/video_hashes.cache'

# FFMPEG Settings
clip_duration=5
clip_fps=10
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
        file_basename = os.path.splitext(video_file)[0]
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
hash_set = load_hash_cache(hash_cache_file)

# Create the subdirectory for the resulting GIF files and metadata
# This is the process for a single file:
if video_file is not None:
    if not os.path.exists(file_basename):
        os.mkdir(file_basename)
    md5 = dump_md5(video_file)
    if md5 in hash_set:
        sys.exit('Aborting! This file has already been processed')

    detect_scenes(video_file, file_basename)
    create_thumbs(video_file, clip_duration = clip_duration, clip_fps = clip_fps, clip_scale = clip_scale)
    dump_md5(video_file, file_basename)
    dump_video_metadata(video_file, file_basename)
else:
    for file in files_list:
        print file

sys.exit()   

    
# s_duration = subprocess.check_output(['ffprobe', '-hide_banner', '-i', video_file, '-show_entries', 'format=duration', '-v', 'quiet', '-of', 'csv=%s' % ('p=0')])
# f_duration = float(s_duration.strip())
# i_duration = int(f_duration)
# 
# if args.verbose is True:
#     print('Video File Name: %s' % video_file)
#     print('Float Duration: %f' % f_duration)
#     print('Int Duration: %d' % i_duration)




# if this is a single file, process it an exit



# if this is a list of files 

file_part=1
if os.path.getsize('%s.ts' % file_basename) > 0:
    with open('%s.ts' % file_basename, 'r') as f:
        for timestamp in f:
            pad = '%03d' % file_part
            subprocess.call(['ffmpeg', '-hide_banner', '-y', '-ss', '%f' % float(timestamp), '-t', str(clip_duration), '-i', video_file, '-vf', 'fps=%s,scale=%s:-1:flags=lanczos,palettegen' % (clip_fps, clip_scale), 'palette-%s.png' % (pad)])
            subprocess.call(['ffmpeg', '-hide_banner', '-ss', '%f' % float(timestamp), '-t', str(clip_duration), '-i', video_file, '-i', 'palette-%s.png' % (pad), '-filter_complex', 'fps=%s,scale=%s:-1:flags=lanczos[x];[x][1:v] paletteuse' % (clip_fps, clip_scale), '%s/%s-%s.gif' % (file_basename, file_basename, pad)])
            os.remove('palette-%s.png' % pad)
            subprocess.call(['ffmpeg', '-hide_banner', '-ss', '%f' % float(timestamp), '-i', video_file, '-vframes', '1', '-vf', 'scale=%s:-1' % (clip_scale), '%s/%s-%s.png' % (file_basename, file_basename, pad)])
            file_part += 1
else:
    timestamp = 5
    pad = '%03d' % file_part
    subprocess.call(['ffmpeg', '-hide_banner', '-y', '-ss', '%f' % float(timestamp), '-t', str(clip_duration), '-i', video_file, '-vf', 'fps=%s,scale=%s:-1:flags=lanczos,palettegen' % (clip_fps, clip_scale), 'palette-%s.png' % (pad)])
    subprocess.call(['ffmpeg', '-hide_banner', '-ss', '%f' % float(timestamp), '-t', str(clip_duration), '-i', video_file, '-i', 'palette-%s.png' % (pad), '-filter_complex', 'fps=%s,scale=%s:-1:flags=lanczos[x];[x][1:v] paletteuse' % (clip_fps, clip_scale), '%s/%s-%s.gif' % (file_basename, file_basename, pad)])
    os.remove('palette-%s.png' % pad)
    subprocess.call(['ffmpeg', '-hide_banner', '-ss', '%f' % float(timestamp), '-i', video_file, '-vframes', '1', '-vf', 'scale=%s:-1' % (clip_scale), '%s/%s-%s.png' % (file_basename, file_basename, pad)])

dump_md5(video_file, file_basename)
dump_video_metadata(video_file, file_basename)

