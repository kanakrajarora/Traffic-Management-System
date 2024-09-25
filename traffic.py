import cv2
import numpy as np

# Load YOLO
net = cv2.dnn.readNet("C:/Users/kanak/Downloads/Buzz Earth/yolov3.weights", "C:/Users/kanak/Downloads/Buzz Earth/yolov3.cfg")
with open("C:/Users/kanak/Downloads/Buzz Earth/archive/vehicle dataset/classes.txt", encoding="utf-8") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

# Initialize video capture (use your video source, e.g., 'video.mp4' or 0 for webcam)
cap = cv2.VideoCapture("C:/Users/kanak/Downloads/Buzz Earth/2103099-uhd_3840_2160_30fps.mp4")

# Function to draw grid on the frame
def draw_grid(frame, rows, cols):
    height, width, _ = frame.shape
    for i in range(1, rows):
        cv2.line(frame, (0, i * height // rows), (width, i * height // rows), (255, 255, 255), 1)
    for j in range(1, cols):
        cv2.line(frame, (j * width // cols, 0), (j * width // cols, height), (255, 255, 255), 1)

# Function to detect and count vehicles
def detect_and_count(frame):
    height, width, _ = frame.shape
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outputs = net.forward(output_layers)

    class_ids = []
    confidences = []
    boxes = []
    
    # Process detections
    for output in outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.7:  # Adjust confidence threshold as needed
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)  # Apply non-max suppression

    vehicle_count = 0
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            # Ensure the class_id is valid
            if class_ids[i] < len(classes):
                label = str(classes[class_ids[i]])
                if label in ["car", "threewheel", "bus", "truck", "motorbike", "van"]:  # Specify vehicle classes
                    vehicle_count += 1
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Draw bounding box
                    cv2.putText(frame, label, (x, y + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    return vehicle_count

# Main loop
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize the frame while maintaining aspect ratio
    height, width = frame.shape[:2]
    aspect_ratio = width / height
    new_width = 640
    new_height = int(new_width / aspect_ratio)
    
    # Resize the entire frame
    frame = cv2.resize(frame, (new_width, new_height))

    draw_grid(frame, 4, 4)  # Adjust grid size (rows, cols)
    vehicle_count = detect_and_count(frame)
    
    # Logic for triggering traffic signal
    if vehicle_count > 10:  # Change threshold based on your requirements
        cv2.putText(frame, "GREEN LIGHT", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    else:
        cv2.putText(frame, "RED LIGHT", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
