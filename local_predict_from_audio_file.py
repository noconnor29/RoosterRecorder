import os

from micmon.audio import AudioFile
from micmon.model import Model

model_dir = os.path.expanduser('~/rooster_recorder/models/rooster')
model = Model.load(model_dir)
cur_seconds = 60
sample_duration = 4 

with AudioFile('~/rooster_recorder/datasets/sound-detect/audio/train_sample_1/audio.mp3', start=cur_seconds, duration='10:00',
               sample_duration=sample_duration) as reader:
    for sample in reader:
        prediction = model.predict(sample)
        print(f'Audio segment at {cur_seconds} seconds: {prediction}')
        cur_seconds += sample_duration
