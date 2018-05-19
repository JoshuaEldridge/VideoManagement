#!/bin/bash

start_time=952
duration=3.5

palette="/tmp/palette.png"

filters="fps=15,scale=320:-1:flags=lanczos"
base=$(basename "$1")
output_file=${base%.*}-$start_time.gif
echo $base $output_file
ffmpeg -v warning -ss $start_time -t $duration -i $1 -vf "$filters,palettegen" -y $palette
ffmpeg -v warning -ss $start_time -t $duration -i $1 -i $palette -lavfi "$filters [x]; [x][1:v] paletteuse" -y $output_file

# ffmpeg -hide_banner -ss 0 -i "Reel-1001-03.mov" -vframes 1 -vf scale=418:320 "Reel-1001-03/Reel-1001-03-000.png"

ffmpeg -ss 952 -i Reel-1003-01.mp4 -t 3 -vf scale=320:180 -c:v libx264 -c:a aac -strict experimental -b:a 128k output.mp4

