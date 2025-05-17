# ROS_Gate_Control
# ROS 2 Automated Gate Control System

This project implements an automated gate control system using an Arduino and ROS 2, integrating hardware sensors with real-time visualization in RViz.

---

## 🧰 Hardware Components

- **Ultrasonic Sensor (HC-SR04):**  
  Measures distance to detect objects in front of the gate.

- **Servo Motor:**  
  Operates the gate by rotating between open and closed positions.

- **Arduino UNO:**  
  Handles sensor data acquisition and servo control.

- **ROS 2 Machine (Ubuntu):**  
  Runs ROS 2 nodes, processes serial data, and visualizes the system in RViz.

- **USB Serial Communication:**  
  Facilitates data exchange between Arduino and ROS 2.

---

## 🧱 Software Architecture

### Arduino Firmware
- Measures distance using the ultrasonic sensor.
- Operates the gate using the servo motor.
- Sends distance data via serial to the ROS 2 system.

### ROS 2 Python Node (`arduino_reader_node`)
- Reads distance values from the serial port.
- Publishes `std_msgs/Int32` messages to the `/ultrasonic_distance` topic.
- Implements logic to determine and control gate state.
- Publishes `visualization_msgs/Marker` messages for RViz representation.

---

## 🚦 Implementation

### Arduino Code
- Initializes the ultrasonic sensor and servo motor.
- Continuously measures distance.
- Opens the gate if the distance is less than 15 cm.
- Closes the gate after a delay when the object moves away.
- Sends distance data via USB serial to the ROS 2 system.

### ROS 2 Python Node
- Reads serial data from `/dev/ttyUSB0`.
- Parses the distance and publishes it to a ROS topic.
- Controls the gate state using threshold logic.
- Publishes two RViz markers:
  - **Blue cube** representing the approaching vehicle (position based on distance).
  - **Green or black gate marker** (green when open, black when closed).

---

## 🖥️ Visualization

Using **RViz**, a dynamic scene is displayed with:

- A vehicle marker moving closer or farther based on the detected distance.
- A gate marker that changes color to represent open (green) or closed (black) status.

---

## 📦 Requirements

- Arduino IDE
- ROS 2 (tested on ROS 2 Humble)
- Python 3 with `pyserial` and `rclpy`
- RViz2

---


## 📜 License

This project is open-source and available under the MIT License.
