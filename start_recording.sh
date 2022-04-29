#!/bin/bash
pkill -f timestamp
ps ax | grep ffmpeg | awk -F ' ' '{print $1}}' | xargs sudo kill -9
sleep 60
/usr/bin/python3 -u /home/pi/rooster_recorder/timestamp_predict_from_microphone.py >> /home/pi/rooster_recorder/datasets/sound-detect/logs/`date +%m-%d-%Y`.log 2>&1 |/usr/bin/logger -t ROOSTER 
