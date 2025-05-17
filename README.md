# ROS_Gate_Control
Hardware Components
•	Ultrasonic Sensor (HC-SR04): Measures distance to detect objects in front of the gate.
•	Servo Motor: Operates the gate by rotating between open and closed positions.
•	Arduino UNO: Handles sensor data acquisition and servo control.
•	ROS 2 Machine (Ubuntu): Runs ROS 2 nodes, processes serial data, and visualizes the system in RViz.
•	USB Serial Communication: Facilitates data exchange between Arduino and ROS 2.
Software Architecture
•	Arduino Firmware:
o	Measures distance using ultrasonic sensor.
o	Operates gate using servo motor.
o	Sends distance data via serial to ROS 2.
•	ROS 2 Python Node (arduino_reader_node):
o	Reads distance values from serial.
o	Publishes std_msgs/Int32 messages to ultrasonic_distance topic.
o	Controls logic to determine gate state.
o	Publishes RViz visualization_msgs/Marker messages for gate and vehicle representation.
Implementation
Arduino Code
•	Initializes the ultrasonic sensor and servo motor.
•	Continuously measures distance and opens the gate if distance < 15 cm.
•	After a delay, closes the gate if the object moves away.
•	Sends distance data via USB serial to ROS 2.
ROS 2 Python Node
•	Reads serial data from /dev/ttyUSB0 and parses the distance.
•	Publishes the distance to a ROS topic.
•	Controls gate state using a simple thresholding logic.
•	Publishes two Marker messages:
o	A blue cube representing the approaching vehicle (positioned based on distance).
o	A green or black gate marker (green when open, black when closed).
Visualization
•	RViz is used to display a dynamic scene with:
o	The vehicle marker moving closer or farther based on distance.
o	The gate changing color to indicate open/closed status.
