#!/usr/bin/python
from __future__ import print_function
import os
import gzip
from sets import Set

video_hashes_file = '/Volumes/500GBHD/Users/josh/Pictures/Photos/20180520202313.hashes.csv.gz'
known_md5s = set()

f = gzip.open(video_hashes_file, 'rb')

contents = f.read().splitlines()

for i in contents:
    pieces = [x.strip() for x in i.split(',')]
    if pieces[2] in known_md5s:
        print("collision: %s" % pieces)
    else:
        known_md5s.add(pieces[2])

# print(known_md5s)
print(len(known_md5s))
