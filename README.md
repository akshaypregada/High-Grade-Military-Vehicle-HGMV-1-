# High-Grade Military Vehicle (HGMV-1)

🚀 **An AI-powered Unmanned Ground Vehicle (UGV) for Military Surveillance and Autonomous Navigation**

This project integrates CNN-based object detection, LIDAR-based obstacle avoidance, GPS-based autonomous navigation, and a Gazebo simulation to create an intelligent robotic system for military applications.

---

## 📌 Getting Started

### 1️⃣ Flash ESP32 & Arduino Firmware
Upload the following files to your respective microcontrollers:

- **ESP32:** `camera_feed.ino`
- **Arduino Mega:** `motor_control.ino`, `gps_navigation.ino`

### 2️⃣ Run ROS Modules

#### (A) Launch Gazebo Simulation
```sh
roslaunch hgmv1_gazebo_model hgmv1.launch
```

#### (B) Start Object Detection
```sh
rosrun ros_control cnn_model.py
```

#### (C) Start GPS-Based Navigation
```sh
rosrun ros_control gps_navigation.py
```

#### (D) Run LIDAR Obstacle Detection
```sh
rosrun ros_control lidar_processing.py
```

### 3️⃣ Access Web Control Interface
Open `control_panel.html` in a web browser.

- **Live Camera Feed:** Streamed from the ESP32 camera.
- **Real-Time Control Buttons:** Move forward, backward, and stop the UGV.
- **Object Detection Display:** Shows detected objects.

---

## 📌 How It Works

### 🔹 Object Detection Using YOLOv8
- Uses **YOLOv8** for real-time person and vehicle detection.
- Runs inference on images received from the ESP32 camera.
- Displays bounding boxes on detected objects.

### 🔹 GPS-Based Autonomous Navigation
- Receives **latitude & longitude** coordinates.
- Uses **ROS Navigation Stack** to autonomously move toward the goal.
- Integrates with **Gazebo** for simulation testing.

### 🔹 LIDAR-Based Obstacle Avoidance
- Uses **LIDAR sensor data** to avoid objects dynamically.
- Detects the closest obstacle and modifies the path accordingly.

### 🔹 Web-Based Control Panel
- Controls UGV movement via buttons.
- Displays live camera feed.
- Shows real-time LIDAR & GPS data.

---

## 📌 Dependencies

### 🔹 Install ROS and Required Packages
```sh
sudo apt update && sudo apt install -y ros-noetic-desktop-full
sudo apt install -y ros-noetic-gazebo-ros ros-noetic-robot-state-publisher ros-noetic-rviz
```

### 🔹 Install Python Dependencies
```sh
pip install opencv-python torch torchvision ultralytics numpy
```

---
