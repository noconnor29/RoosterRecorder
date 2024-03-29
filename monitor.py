import os
import time

from micmon.audio import AudioDevice
from micmon.model import Model

from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS

## Remove later
from datetime import datetime
from dateutil import tz
log_dir = os.path.expanduser('~/rooster_recorder/datasets/sound-detect/logs')

# Path to a previously saved sound detection Tensorflow model
model_dir = os.path.expanduser('~/rooster_recorder/models/sound-detect')
model = Model.load(model_dir)

AUDIO_SYSTEM = 'alsa'        # Supported: alsa and pulse
AUDIO_DEVICE = 'plughw:1,0'  # Get list of recognized input devices with arecord -l

TOKEN = "-vGw59rZiARTpsmGvyeUQZaIuplxCPq6n-cwnWrVoTebuV1sJjHnZjnzfhT1ll2UJ3D7YlcIo1vLRvSfiFsyWg=="
URL = "http://10.1.50.29:8086"
ORG = "nodv"
BUCKET = "rooster_metrics"

with AudioDevice(AUDIO_SYSTEM, device=AUDIO_DEVICE) as source:
    for sample in source:
        now = datetime.now(tz = tz.tzlocal())
        dt_string = now.strftime("%m-%d-%Y %H:%M:%S\n")
        date = now.strftime("%m-%d-%Y")
        source.pause()  # Pause recording while we process the frame
        prediction = model.predict(sample)
        if prediction == "positive":
            with InfluxDBClient(url=URL, token=TOKEN, org=ORG) as client:
                write_api = client.write_api(write_options=SYNCHRONOUS)
                DATA = "crow detection=True"
                write_api.write(BUCKET, ORG, DATA, time_precision='s')
                client.close()
            with open(os.path.join(log_dir, str(date + ".log")), "a") as file:
                file.write(str(prediction + " " + dt_string))
        time.sleep(3) # Detection cooldown
        source.resume() # Resume recording
