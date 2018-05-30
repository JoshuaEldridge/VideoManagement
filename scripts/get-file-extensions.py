#!/usr/bin/python

# This is a simple script to sort photo files by their name and
# should only be used on photos that have been renamed to fit this
# specific naming convention: %Y%M%D%H%M%S.jpg

import os
import argparse

from helper_functions import *

parser = argparse.ArgumentParser()

parser.add_argument('dir',  help='path to the directory to scan for files. example: /Volumes/2TB-WD-Elements/DV Library Backup/')

args = parser.parse_args()

results = scan_extensions(args.dir)
print(results)