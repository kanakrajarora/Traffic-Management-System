# Optimizing-Public-Transport-Efficiency

This project is an AI-based traffic management solution aimed at optimizing traffic flow using real-time vehicle detection, distance calculations, and route optimization. It integrates with existing traffic systems and public transport networks to reduce congestion and enhance urban mobility.

## **Overview**
This system uses the YOLOv3 object detection model to identify and count vehicles from video feeds, adjusting traffic signals dynamically based on traffic density. Additionally, the system calculates distances  optimizes routes using graph-based algorithms like Dijkstra or A*..

## **Key Features**
- **Real-time Vehicle Detection**
- **Distance Calculation**

## **Core Technologies**
- **YOLOv3**: For real-time vehicle detection.
- **OpenCV**: For video processing and drawing bounding boxes on detected vehicles.

## **Installation**
### Prerequisites
- Python 3.8+
- Required Libraries:
  ```bash
  pip install opencv-python numpy flask pandas networkx requests
  ```
- Download YOLOv3 weights and configuration files from [YOLO official website](https://pjreddie.com/darknet/yolo/).

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/kanakrajarora/Traffic-Management-System.git
   cd Traffic-Management-System
   ```
2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

## **Future Potential**
- Integration with city traffic systems and public transport providers.
- Expand to handle multiple intersections in real time.
- Incorporate more complex traffic behavior using AI/ML models.

## **License**
This project is licensed under the MIT License.
