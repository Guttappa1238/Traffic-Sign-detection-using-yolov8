from ultralytics import YOLO

model = YOLO("yolov8s.pt")

results = model.train(
        batch=16,
        device="0",
        data="/home/prixgen-gpu/Downloads/images/data.yaml",
        epochs=300,
        imgsz=1280,
    )