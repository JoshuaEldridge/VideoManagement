#!/usr/bin/python
from __future__ import print_function
import os
from helper_functions import *
import argparse
import shutil

parser = argparse.ArgumentParser()

parser.add_argument('dir',  help='path to the directory to scan for files. example: /Volumes/2TB-WD-Elements/DV Library Backup/')
parser.add_argument('-e', '--ext',  help='file extensions to match against. Must be a single extension or a tuple of extensions: (".jpg", ".gif")', default=('.jpg', '.mov', 'png', '.mp4', '.jpeg'))

# Might want to add support for single files, or a possibly a text file with file paths:
#group.add_argument('-l', '--list',  help='list of files to process. example: files-to-process.txt')
#group.add_argument('-f', '--filename', help='name of the video file. example: 20111022144212.mov')

args = parser.parse_args()

home = os.path.expanduser("~")


if os.path.isdir(args.dir) and os.access(args.dir, os.W_OK):
    files_directory = args.dir
    files_list = find_my_files(files_directory, args.ext)
else:
    sys.exit('Error: Directory is not valid or is not writable!')

for file in files_list:
    file_parts = clean_path(file)
    if file_parts['abs'].lower().endswith(args.ext):
        year, month = file_parts['name'][0:4], file_parts['name'][4:6]
        if not os.path.isdir(os.path.join(file_parts['dir'], year)):
            os.mkdir(os.path.join(file_parts['dir'], year))
        if not os.path.isdir(os.path.join(file_parts['dir'], year, month)):
            os.mkdir(os.path.join(file_parts['dir'], year, month))
        print("Moving {0} to {1}/{2}/{3}".format(file_parts['abs'], year, month, file_parts['file']))
        shutil.move(file_parts['abs'], os.path.join(file_parts['dir'], year, month, file_parts['file']))