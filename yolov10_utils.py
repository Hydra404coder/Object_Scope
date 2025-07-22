from ultralytics import YOLO
from cvzone.Utils import putTextRect
import cv2

# Load the model
model = YOLO("yolov10n.pt")  # Make sure this file exists in your folder

def detect_objects(frame):
    results = model(frame)
    annotated_frame = results[0].plot()

    putTextRect(annotated_frame, "Cool project", (10, 30), scale=2, thickness=2, colorR=(0, 255, 0))

    return annotated_frame
