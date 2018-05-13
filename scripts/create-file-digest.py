#!/usr/bin/python

import csv
import os
import hashlib
import platform
from datetime import datetime


video_dir = '/Volumes/HTS-1.5TB/Home Video/VHS CAPTURE/LifeFlix/Tapes'
csv_logfile = os.path.join(video_dir, 'video_file_hashes.csv')
csv_logfile_header = ['MD5 Hash', 'Host', 'File Location', 'File Name', 'File Date']


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
	for root, dirs, files in os.walk(video_dir):
# 		print root, dirs, files
		for file_ in files:		
			if file_.endswith(".mov"):
				path = os.path.join(root, file_)
				csv_writer.writerow([md5(path), 'Betty', video_dir, file_, creation_date(path)])
				print("Wrote: %s, %s, %s, %s, %s" % (md5(path), 'Betty', video_dir, file_, creation_date(path)))