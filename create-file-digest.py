#!/usr/bin/python

import csv
import os
import hashlib
import platform
from datetime import datetime
import subprocess

video_dir = '/Users/josh/Movies/Zi8-Downloaded Videos/'
csv_logfile = video_dir + 'video_file_hashes.csv'
csv_logfile_header = ['MD5 Hash', 'Host', 'File Location', 'File Name', 'File Date', 'Video Metadata Date']

def creation_date(path_to_file):
    """
    Try to get the date that a file was created, falling back to when it was
    last modified if that isn't possible.
    See http://stackoverflow.com/a/39501288/1709587 for explanation.
    """
    if platform.system() == 'Windows':
        return datetime.fromtimestamp(os.path.getctime(path_to_file))
    else:
        stat = os.stat(path_to_file)
        try:
            return datetime.fromtimestamp(stat.st_birthtime)
        except AttributeError:
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
            return datetime.fromtimestamp(stat.st_mtime)



def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

with open(csv_logfile, 'a+') as f:
	csv_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	csv_writer.writerow(csv_logfile_header)
	
	for file in os.listdir(video_dir):
		if file.endswith(".mov"):
			path = os.path.join(video_dir, file)
			md_date = subprocess.check_output(['ffprobe', '-v', 'quiet', path, '-print_format', 'compact', '-show_entries', 'format_tags=creation_time'])
			md_date = md_date.strip().split('format|tag:creation_time=')[1]
			csv_writer.writerow([md5(path), 'Betty', video_dir, file, creation_date(path), md_date])