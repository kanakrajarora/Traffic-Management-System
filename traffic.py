from ultralytics import YOLO
import torch
import cv2
import numpy as np
import matplotlib.pyplot as plt
from google.colab.patches import cv2_imshow  

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

model = YOLO("yolov8n.pt").to(device)

cap = cv2.VideoCapture("/content/2103099-uhd_3840_2160_30fps.mp4")

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps = int(cap.get(cv2.CAP_PROP_FPS))

out = cv2.VideoWriter("output.mp4", cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, device=device)  
    vehicle_count = len(results[0].boxes)

    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    cv2.putText(frame, f"Vehicles: {vehicle_count}", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    out.write(frame)

    # Convert BGR to RGB for displaying in Colab
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    plt.imshow(frame_rgb)
    plt.axis("off")
    plt.show()

cap.release()
out.release()
cv2.destroyAllWindows()

# Download the video file
from google.colab import files
files.download("output.mp4")

