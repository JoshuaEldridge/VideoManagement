#!/usr/bin/python
# Quick tool for examining the various file extensions
# to help determine which ones to filter on.

import os
import subprocess
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

# Probe the video file to detect scene changes, write out the results to a .ts file
def detect_scenes(video_file, file_basename = None, threshold = 0.4):
    # Check to see if the file comes in with a system path
    # if so, handle it properly
    dirname = os.path.dirname(video_file)
    filename = os.path.basename(video_file)
    if dirname is not None:
        os.chdir(dirname)
    if file_basename is None:
        file_basename = os.path.splitext(filename)[0]
    if not os.path.exists(file_basename):
        os.mkdir(file_basename)
    ffprobe_output = subprocess.check_output(['ffprobe', '-hide_banner', '-show_frames', '-print_format', 'compact', '-f', 'lavfi', "movie='%s',select='gt(scene,%f)'" % (video_file, threshold)])
    with open('%s/%s.ffmpeg' % (file_basename, file_basename), 'w') as f:
        f.write(ffprobe_output)
    with open('%s/%s.ts' % ((file_basename, file_basename)), 'w') as o:
        with open('%s/%s.ffmpeg' % (file_basename, file_basename), 'r') as f:
            for s in f:
                for i in s.strip().split("|"):
                    if i.startswith('best_effort_timestamp_time'):
                        ts = i.split("=")[1]
                        o.write('%s\n' % ts)
#                        os.remove('%s.ffmpeg' % file_basename)

def create_thumbs(video_file, file_basename = None, clip_duration = 5, clip_fps = 15, clip_scale = 320, timestamp = 5, file_part = 1):
    if file_basename is None:
        file_basename = os.path.splitext(video_file)[0]
    pad = '%03d' % file_part
    subprocess.call(['ffmpeg', '-hide_banner', '-y', '-ss', '%f' % float(timestamp), '-t', str(clip_duration), '-i', video_file, '-vf', 'fps=%s,scale=%s:-1:flags=lanczos,palettegen' % (clip_fps, clip_scale), 'palette-%s.png' % (pad)])
    subprocess.call(['ffmpeg', '-hide_banner', '-ss', '%f' % float(timestamp), '-t', str(clip_duration), '-i', video_file, '-i', 'palette-%s.png' % (pad), '-filter_complex', 'fps=%s,scale=%s:-1:flags=lanczos[x];[x][1:v] paletteuse' % (clip_fps, clip_scale), '%s/%s-%s.gif' % (file_basename, file_basename, pad)])
    os.remove('palette-%s.png' % pad)
    subprocess.call(['ffmpeg', '-hide_banner', '-ss', '%f' % float(timestamp), '-i', video_file, '-vframes', '1', '-vf', 'scale=%s:-1' % (clip_scale), '%s/%s-%s.png' % (file_basename, file_basename, pad)])


# Dump all the video metadata to a json file
def dump_video_metadata(video_file, file_basename = None):
    if file_basename is None:
        file_basename = os.path.splitext(video_file)[0]
    video_metadata = '%s/%s.json' % (file_basename, file_basename)
    with open(video_metadata, 'w') as f:
        json_output = subprocess.check_output(['ffprobe', '-hide_banner', '-v', 'quiet', '-print_format', 'json', '-show_format', '-show_streams', video_file])
        f.write(json_output)

def dump_md5(video_file, file_basename = None):
    if file_basename is None:
        file_basename = os.path.splitext(video_file)[0]
    video_md5_file = '%s/%s.md5' % (file_basename, file_basename)
    video_md5_hash = md5(video_file)
    with open(video_md5_file, 'w') as f:
        f.write(video_md5_hash)
    return video_md5_hash
    
def load_hash_cache(cache_file):
    if os.path.isfile(cache_file)  and os.access(cache_file, os.R_OK):
        with open(cache_file, 'r') as f:
            return set([line.rstrip() for line in f])
    else:
        return set()

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