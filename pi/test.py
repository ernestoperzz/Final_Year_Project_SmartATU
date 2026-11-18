from picamera2 import Picamera2
import time



picam2 = Picamera2()
picam2.configure(picam2.create_still_configuration())
picam2.options["quality"] = 95  

picam2.start()
time.sleep(2)                    
picam2.autofocus_cycle()         
picam2.capture_file("image.jpg")
picam2.stop()
picam2.close()





