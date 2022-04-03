# RoosterRecorder
Small project to monitor and analyze loud sounds (ex. neighborhood roosters)

## Objectives
 - automatically identify target sounds with accuracy from background noise
 - log data to create statistics about event frequency 
 - use data and statistics to generate trends and charts

## Ideal Case
 - continuously cache last X seconds of sound to RAM
 - upon detection of sound Y dB above threshold), write Z seconds from before/after detection to file
 - write event data to log file:
   - date, time, running event ID (or restart event ID daily?)
 - analyze recording for waveform. save waveform as image.

## Requirements
 - Raspberry Pi (Wi-Fi and power)
 - USB microphone
 - Remote file storage (ideally write-only) 
 - python
