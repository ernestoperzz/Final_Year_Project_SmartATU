from picamera2 import Picamera2
import time
from ultralytics import YOLO

model = YOLO("yolov8m.pt")

picam2 = Picamera2()
picam2.configure(picam2.create_still_configuration())
picam2.options["quality"] = 95   # sharper JPEGs

picam2.start()
time.sleep(2)                    # let brightness and colour adjust
picam2.autofocus_cycle()         # focus before the photo
picam2.capture_file("image.jpg")
picam2.stop()

results = model.predict("image.jpg")
result = results[0]
len(result.boxes)
box = result.boxes[0]
print("Object type:",box.cls[0])
print("Coordinates:",box.xyxy[0])
print("Probability:",box.conf[0])
cords = box.xyxy[0].tolist()
class_id = box.cls[0].item()
conf = box.conf[0].item()
print("Object type:", class_id)
print("Coordinates:", cords)
print("Probability:", conf)
print(result.names)