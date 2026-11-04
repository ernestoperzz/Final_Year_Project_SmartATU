#just recroding a video in this script


import time
from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput

picam2 = Picamera2()
picam2.configure(picam2.create_video_configuration(main = {"size": (640, 480)}))

encoder = H264Encoder(bitrate=5_000_000)
picam2.start_recording(encoder, FfmpegOutput("clip.mp4"))
time.sleep(5)
picam2.stop_recording()


  