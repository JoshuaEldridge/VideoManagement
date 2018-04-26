#!/usr/bin/python

import json
from pprint import pprint 
with open('Reel-1001-01.json') as f:
    md = json.load(f)

for i in md['streams']:
    pprint(i)
# pprint(md)