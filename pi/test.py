from picamera2 import Picamera2
import time
from ultralytics import YOLO

model = YOLO("yolov8m.pt")

picam2 = Picamera2()
picam2.configure(picam2.create_still_configuration())
picam2.options["quality"] = 95  

picam2.start()
time.sleep(2)                    
picam2.autofocus_cycle()         
picam2.capture_file("image.jpg")
picam2.stop()
picam2.close()


results = model.predict("image.jpg")
result = results[0]
len(result.boxes)


for box in result.boxes:
  class_id = result.names[box.cls[0].item()]
  cords = box.xyxy[0].tolist()
  cords = [round(x) for x in cords]
  conf = round(box.conf[0].item(), 2)
  print("Object type:", class_id)
  print("Coordinates:", cords)
  print("Probability:", conf)
  print("---")