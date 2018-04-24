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
import hashlib

parser = argparse.ArgumentParser()
parser.add_argument('filename', help='name of the video file. example: 20111022144212.mov')
parser.add_argument('-v', '--verbose', default=True)
args = parser.parse_args()
video_file = args.filename
file_basename = os.path.splitext(video_file)[0]

def check_lib(name):
    from distutils.spawn import find_executable
    return find_executable(name) is not None
    
# First check that all permissions are valid:
# 0. Required libraries (ffmpeg, ffprobe) are installed and available
# 1. File is readable and directory is writable, so we can create a subfolder for assets
# 2.

# 0. Check for required libraries
if check_lib('ffmpeg') and check_lib('ffprobe') is None:
    sys.exit('Error: This script requires ffmpeg and ffprobe libraries be available in the $PATH!')

# 1. Check for permissions
if not os.access(os.getcwd(), os.W_OK) or not os.access(video_file, os.R_OK):
    sys.exit('Error: Directory is writable and file is readable!')

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()
    
s_duration = subprocess.check_output(['ffprobe', '-i', video_file, '-show_entries', 'format=duration', '-v', 'quiet', '-of', 'csv=%s' % ('p=0')])
f_duration = float(s_duration.strip())
i_duration = int(f_duration)

# Based on the duration of the video, determine the number of segments
# Minimally, create two segments twenty at most, otherwise every three minutes


if args.verbose is True:
    print('Video File Name: %s' % video_file)
    print('Float Duration: %f' % f_duration)
    print('Int Duration: %d' % i_duration)


# FFMPEG Settings
clip_duration=5
clip_fps=10
clip_scale=320

# Create the subdirectory for the resulting GIF files and metadata
os.mkdir(file_basename)
    
file_part=1

if os.path.getsize('%s.ts' % file_basename) > 0:
    with open('%s.ts' % file_basename, 'r') as f:
        for timestamp in f:
            pad = '%03d' % file_part
            subprocess.call(['ffmpeg', '-y', '-ss', '%f' % float(timestamp), '-t', str(clip_duration), '-i', video_file, '-vf', 'fps=%s,scale=%s:-1:flags=lanczos,palettegen' % (clip_fps, clip_scale), 'palette-%s.png' % (pad)])
            subprocess.call(['ffmpeg', '-ss', '%f' % float(timestamp), '-t', str(clip_duration), '-i', video_file, '-i', 'palette-%s.png' % (pad), '-filter_complex', 'fps=%s,scale=%s:-1:flags=lanczos[x];[x][1:v] paletteuse' % (clip_fps, clip_scale), '%s/%s-%s.gif' % (file_basename, file_basename, pad)])
            os.remove('palette-%s.png' % pad)
            subprocess.call(['ffmpeg', '-ss', '%f' % float(timestamp), '-i', video_file, '-vframes', '1', '-vf', 'scale=%s:-1' % (clip_scale), '%s/%s-%s.png' % (file_basename, file_basename, pad)])
            file_part += 1
else:
    timestamp = 1
    pad = '%03d' % file_part
    subprocess.call(['ffmpeg', '-y', '-ss', '%f' % float(timestamp), '-t', str(clip_duration), '-i', video_file, '-vf', 'fps=%s,scale=%s:-1:flags=lanczos,palettegen' % (clip_fps, clip_scale), 'palette-%s.png' % (pad)])
    subprocess.call(['ffmpeg', '-ss', '%f' % float(timestamp), '-t', str(clip_duration), '-i', video_file, '-i', 'palette-%s.png' % (pad), '-filter_complex', 'fps=%s,scale=%s:-1:flags=lanczos[x];[x][1:v] paletteuse' % (clip_fps, clip_scale), '%s/%s-%s.gif' % (file_basename, file_basename, pad)])
    os.remove('palette-%s.png' % pad)
    subprocess.call(['ffmpeg', '-ss', '%f' % float(timestamp), '-i', video_file, '-vframes', '1', '-vf', 'scale=%s:-1' % (clip_scale), '%s/%s-%s.png' % (file_basename, file_basename, pad)])

# Dump all the video metadata to a json file
video_metadata = '%s/%s.json' % (file_basename, file_basename)
with open(video_metadata, 'w') as f:
    json_output = subprocess.check_output(['ffprobe', '-v', 'quiet', '-print_format', 'json', '-show_format', '-show_streams', video_file])
    f.write(json_output)

video_md5_file = '%s/%s.md5' % (file_basename, file_basename)
video_md5_hash = md5(video_file)
with open(video_md5_file, 'w') as f:
    f.write(video_md5_hash)