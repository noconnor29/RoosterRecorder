import os
import time

from micmon.audio import AudioDevice
from micmon.model import Model
from datetime import datetime
from dateutil import tz

# Path to a previously saved sound detection Tensorflow model
model_dir = os.path.expanduser('~/rooster_recorder/models/sound-detect')
model = Model.load(model_dir)

audio_system = 'alsa'        # Supported: alsa and pulse
audio_device = 'plughw:1,0'  # Get list of recognized input devices with arecord -l

with AudioDevice(audio_system, device=audio_device) as source:
    for sample in source:
        now = datetime.now(tz = tz.tzlocal())
        dt_string = now.strftime("%m-%d-%Y %H:%M:%S\n") 
        source.pause()  # Pause recording while we process the frame
        prediction = model.predict(sample)
        if prediction == "positive":
            with oprn(os.path.join(model_dir, "logs", str(date + ".log")), "a") as file:
                file.write(str(prediction + " " + dt_string))
        time.sleep(3) # Detection cooldown
        source.resume() # Resume recording
