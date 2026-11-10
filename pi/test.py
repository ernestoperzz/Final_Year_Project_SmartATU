#just recroding a video in this script


import time
from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput
from libcamera import controls


picam2 = Picamera2()

picam2.configure(picam2.create_video_configuration(main = {"size": (1280, 720)}))
# continuous autofocus (for video and streams)
picam2.set_controls({"AfMode": controls.AfModeEnum.Continuous})

encoder = H264Encoder(bitrate=5_000_000)
picam2.start_recording(encoder, FfmpegOutput("clip.mp4"))
time.sleep(5)
picam2.stop_recording()


  