#!/bin/bash

start_time=0
duration=10

palette="/tmp/palette.png"

filters="fps=15,scale=320:-1:flags=lanczos"

# ffmpeg -v warning -ss $start_time -t $duration -i $1 -vf "$filters,palettegen" -y $palette
# ffmpeg -v warning -ss $start_time -t $duration -i $1 -i $palette -lavfi "$filters [x]; [x][1:v] paletteuse" -y $2
ffmpeg -hide_banner -ss 0 -i "Reel-1001-03.mov" -vframes 1 -vf scale=418:320 "Reel-1001-03/Reel-1001-03-000.png"