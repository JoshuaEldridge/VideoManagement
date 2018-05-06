#!/usr/bin/python
# Quick tool for examining the various file extensions
# to help determine which ones to filter on.

import os
import sys
import subprocess
import pickle
import json
#from collections import Counter

#folder = "/Volumes/2TB-WD-Elements/DV Library Backup/"

#extensions = ('.dv', '.mov', '.mpg', '.avi', '.mp4', '.m4v', '.flv')
# By default this function will return all of the video file types listed out,
# to filter to a specific file type or types, just pass in a tuple with the extensions
def find_my_files(dir, exts = ('.dv', '.mov', '.mpg', '.avi', '.mp4', '.m4v', '.flv')):
    matches = []
    for root, dirnames, filenames in os.walk(dir):
        for filename in filenames:
            if filename.endswith(exts):
                matches.append(os.path.join(root, filename))
    return matches

# Simply check to see if the libraries are found on the system
# and are executable
def check_lib(name):
    from distutils.spawn import find_executable
    return find_executable(name) is not None

# Generate a md5 hash in a memory friendly way
def md5(fname):
    import hashlib
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

# This function will take a file name, fully qualified with path or not
# and return a three item dictionary of the parts
# CHANGES WORKING DIRECTORY!
def clean_path(file):
    file_parts = {}
    file_parts['abs'] = os.path.normpath(os.path.join(os.getcwd(), file))
    file_parts['dir'] = os.path.dirname(file_parts['abs'])
    file_parts['file'] = os.path.basename(file_parts['abs'])
    file_parts['name'] = os.path.splitext(file_parts['file'])[0]
    file_parts['subdir'] = os.path.join(file_parts['dir'], file_parts['name'])
    file_parts['subfile'] = os.path.join(file_parts['subdir'], file_parts['name'])
    return file_parts

# This function expects a file parts dictionary as created by the clean_path function
def dump_md5(file_parts):
    video_md5_file = os.path.join(file_parts['subdir'], '%s.md5' % file_parts['name'])
    video_md5_hash = md5(file_parts['abs'])
    with open(video_md5_file, 'w') as f:
        f.write(video_md5_hash)
    return video_md5_hash

def load_hash_cache(cache_file):
    if os.path.isfile(cache_file)  and os.access(cache_file, os.R_OK):
        return pickle.load(open(cache_file, 'r'))
    else:
        pickle.dump(set(), open(cache_file, "wb"))
        return set()

def get_video_duration(file_parts):
    return subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', file_parts['abs']])

def read_json_duration(file_parts, field = None):
    with open('%s.json' % file_parts['subfile'], 'r') as f:
        md = json.load(f)
        return md['format']['duration']
        
# Probe the video file to detect scene changes, write out the results to a .ts file
def detect_scenes(file_parts, threshold = 0.4):
    ffprobe_output = subprocess.check_output(['ffprobe', '-hide_banner', '-show_frames', '-print_format', 'compact', '-f', 'lavfi', "movie='%s',select='gt(scene,%f)'" % (file_parts['abs'], threshold)])
    with open('%s.ffmpeg' % file_parts['subfile'], 'w') as f:
        f.write(ffprobe_output)
    with open('%s.ts' % file_parts['subfile'], 'w') as o:
        with open('%s.ffmpeg' % file_parts['subfile'], 'r') as f:
            for s in f:
                for i in s.strip().split("|"):
                    if i.startswith('best_effort_timestamp_time'):
                        ts = i.split("=")[1]
                        o.write('%s\n' % ts)
#                        os.remove('%s.ffmpeg' % file_basename)

def create_thumbs(file_parts, clip_duration = 5, clip_fps = 15, clip_scale = 320, timestamp = 5, part = 1, mode = "still"):
    pad = '%03d' % part
    if mode == "still":
        # Only produce a single still image
            subprocess.call(['ffmpeg', '-hide_banner', '-ss', '%f' % float(timestamp), '-i', file_parts['abs'], '-vframes', '1', '-vf', 'scale=%s:-1' % (clip_scale), '%s-%s.png' % (file_parts['subfile'], pad)])
    else:
        subprocess.call(['ffmpeg', '-hide_banner', '-y', '-ss', '%f' % float(timestamp), '-t', str(clip_duration), '-i', file_parts['abs'], '-vf', 'fps=%s,scale=%s:-1:flags=lanczos,palettegen' % (clip_fps, clip_scale), os.path.join(file_parts['subdir'], 'palette-%s.png' % (pad))])
        subprocess.call(['ffmpeg', '-hide_banner', '-ss', '%f' % float(timestamp), '-t', str(clip_duration), '-i', file_parts['abs'], '-i', os.path.join(file_parts['subdir'], 'palette-%s.png' % (pad)), '-filter_complex', 'fps=%s,scale=%s:-1:flags=lanczos[x];[x][1:v] paletteuse' % (clip_fps, clip_scale), '%s-%s.gif' % (file_parts['subfile'], pad)])
        os.remove(os.path.join(file_parts['subdir'], 'palette-%s.png' % (pad)))
        subprocess.call(['ffmpeg', '-hide_banner', '-ss', '%f' % float(timestamp), '-i', file_parts['abs'], '-vframes', '1', '-vf', 'scale=%s:-1' % (clip_scale), '%s-%s.png' % (file_parts['subfile'], pad)])

# Dump all the video metadata to an export file
# Available formats are: default, compact, csv, flat, ini, json, xml
def dump_video_metadata(file_parts, format = 'json'):
    video_metadata = '%s.%s' % (file_parts['subfile'], format)
    with open(video_metadata, 'w') as f:
        output = subprocess.check_output(['ffprobe', '-hide_banner', '-v', 'quiet', '-print_format', format, '-show_format', '-show_streams', file_parts['abs']])
        f.write(output)


# Traverse the directory and count the number of files by their
# extensions. NOTICE: This excludes any files with a single occurance
# 
# ListFiles = os.walk(folder)
# SplitTypes = []
# for walk_output in ListFiles:
#     for file_name in walk_output[-1]:
#         SplitTypes.append(file_name.split(".")[-1])
# 
# counter = Counter(SplitTypes)
# for k, v in counter.items():
#     if v > 1:
#         print k, v