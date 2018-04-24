#!/bin/bash

filename=$1
file_basename=${1%.*}

# echo $filename
# echo $file_basename

ffmpeg -i $filename -filter:v "select='gt(scene,0.4)',showinfo" -f null - 2> /tmp/$file_basename.ffmpeg
cat /tmp/$file_basename.ffmpeg
grep showinfo /tmp/$file_basename.ffmpeg | grep pts_time:[0-9.]* -o | grep '[0-9]*\.[0-9]*' -o > $file_basename.ts
archive-video-scenes.py $1