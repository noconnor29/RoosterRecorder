#!/bin/bash
now=`date +"%m-%d-%Y-%H"`
#END=24
#for ((i=1;i<=END;i++)); do
#	arecord -D plughw:1,0 -c 1 -f cd -d 3600 | lame - audio.mp3
#done
#cd /home/pi/datasets/sound-detect/audio
arecord -D plughw:1,0 -c 1 -f cd -d 3600 | lame - /home/pi/datasets/sound-detect/audio/${now}.mp3
