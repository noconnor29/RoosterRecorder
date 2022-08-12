# RoosterRecorder
Project to monitor and analyze loud sounds (ex. neighborhood roosters)

## Objectives
 - [X] automatically and accurately distinguish target sounds from background noise
 - [X] log data to create statistics about event frequency 
 - [ ] use data and statistics to generate trends and charts

## Requirements
 - Raspberry Pi 3B+ (64-bit, more RAM is better)
 - USB microphone
 - Remote file storage or metrics aggregator endpoint (TIG stack?)
 - python3, tensorflow

## Process
 - Record sample file(s) containing target sound (audio.mp3)
 - Label (labels.json) examples of target sound in sample file(s)
 - Train the model and generate signatures
 - Setup systemd service to monitor and log on boot
   - v1: output positive identifications to daily log file (`wc -l` for count)
   - v2: create connector to push events to logging and analytics service

## Acknowledgements
 - This project would not have been possible without the previous work and detailed instructions of [Fabio Manganiello](https://fabiomanganiello.com/)
   - https://github.com/BlackLight/micmon
   - [Create your own smart baby monitor with a RaspberryPi and Tensorflow](https://towardsdatascience.com/create-your-own-smart-baby-monitor-with-a-raspberrypi-and-tensorflow-5b25713410ca)

## File Structure
```
├── datasets
│   └── sound-detect
│       ├── audio
│       │   └── train_sample_1
│       │       ├── audio.mp3
│       │       └── labels.json
│       ├── addl-samples
│       │   ├── 04-13-2022-23
│       │       ├── 04-13-2022-23.mp3
│       │       └── labels.json
```
