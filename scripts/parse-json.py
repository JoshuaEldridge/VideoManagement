#!/usr/bin/python

import json
from pprint import pprint 
with open('Reel-1001-01.json') as f:
    md = json.load(f)

for v in md['format']:
    print v
    
    
print md['format']['duration']