from ultralytics import YOLO
from PIL import Image
import cv2

model = YOLO("/home/prixgen-gpu/Downloads/DCIL_assignment/runs/detect/train3/weights/best.pt")
# metrics = model.val()
# accepts all formats - image/dir/Path/URL/video/PIL/ndarray. 0 for webcam
# results = model.predict(source="UnSeen_Dataset.mp4", show=True,save=True,imgsz=1280, conf=0.35)

# Perform tracking with the model
# results = model.track(source="https://youtu.be/LNwODJXcvt4", show=True)  # Tracking with default tracker
# results = model.track(source="https://youtu.be/LNwODJXcvt4", show=True, tracker="bytetrack.yaml") 
results = model.track(source="UnSeen_Dataset.mp4", conf=0.15, iou=0.4, show=True,save=True)