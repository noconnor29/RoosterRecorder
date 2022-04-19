import os

from micmon.audio import AudioDevice
from micmon.model import Model
from datetime import datetime


# Path to a previously saved sound detection Tensorflow model
model_dir = os.path.expanduser('~/rooster_recorder/models/sound-detect')
model = Model.load(model_dir)

audio_system = 'alsa'        # Supported: alsa and pulse
audio_device = 'plughw:1,0'  # Get list of recognized input devices with arecord -l

with AudioDevice(audio_system, device=audio_device) as source:
    for sample in source:
        now = datetime.now()
        dt_string = now.strftime("%d-%m-%Y %H:%M:%S") 
        source.pause()  # Pause recording while we process the frame
        prediction = model.predict(sample)
#        if type(prediction) == str:
#            ring
        if prediction == "positive":
            print(prediction, dt_string)
        source.resume() # Resume recordingu
