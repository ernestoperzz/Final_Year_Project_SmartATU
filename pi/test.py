#This is just a simple photo script that will take a photo using the Raspberry Pi camera module and save it to a specified directory.

from picamera2 import Picamera2

picam2 = Picamera2()
config = picam2.create_still_configuration(

main={"size": (4608, 2592)}
)

picam2.configure(config)
picam2.start()
picam2.capture_file("image.jpg")
picam2.stop()