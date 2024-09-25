# Optimizing-Public-Transport-Efficiency

This project is an AI-based traffic management solution aimed at optimizing traffic flow using real-time vehicle detection, distance calculations, and route optimization. It integrates with existing traffic systems and public transport networks to reduce congestion and enhance urban mobility.

## **Overview**
This system uses the YOLOv3 object detection model to identify and count vehicles from video feeds, adjusting traffic signals dynamically based on traffic density. Additionally, the system calculates distances using the Google Maps API and optimizes routes using graph-based algorithms like Dijkstra or A*.

## **Key Features**
- **Real-time Vehicle Detection**: YOLOv3 is used for detecting vehicles such as cars, buses, and trucks from live or recorded video streams.
- **Dynamic Traffic Signal Control**: Traffic lights are controlled based on the real-time vehicle count to reduce waiting times at intersections.
- **Distance Calculation**: Google Maps Distance Matrix API is used to calculate driving distances between pickup and drop-off points.
- **Route Optimization**: Uses NetworkX to model road networks and calculate the shortest path between locations.

## **Core Technologies**
- **YOLOv3**: For real-time vehicle detection.
- **Google Maps API**: For distance calculation between traffic points.
- **NetworkX**: For graph-based analysis and shortest path algorithms.
- **Intel® OpenVINO™ Toolkit**: Used for optimizing AI models for Intel hardware, improving performance.
- **Intel® oneAPI AI Analytics Toolkit**: For accelerated training and inference of traffic detection models.
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
   git clone https://github.com/your-username/traffic-management-system.git
   cd traffic-management-system
   ```
2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Obtain an API key from Google Cloud Platform for the Google Maps Distance Matrix API and update it in the code.

## **Usage**
- The system processes video frames to detect vehicles, count them, and adjust traffic signals based on the vehicle count.
- For real-time video streams, use your webcam or specify a video file path.
- The system outputs the processed video with bounding boxes around detected vehicles and traffic light statuses displayed.

## **Technical Architecture**
1. **Vehicle Detection**: YOLOv3 model detects vehicles from video frames.
2. **Traffic Signal Management**: Based on vehicle count, adjusts traffic light signals.
3. **Distance Calculation**: Google Maps API calculates driving distances.
4. **Route Optimization**: NetworkX computes the shortest route between nodes.

## **Intel Technologies Used**
- **Intel® OpenVINO™ Toolkit**: Optimized vehicle detection model for inference.
- **Intel® AI Analytics Toolkit**: Accelerates model training and inference.
- **Intel® DevCloud for the Edge**: Tested and deployed on edge devices.

## **Future Potential**
- Integration with city traffic systems and public transport providers.
- Expand to handle multiple intersections in real time.
- Incorporate more complex traffic behavior using AI/ML models.

## **License**
This project is licensed under the MIT License.
