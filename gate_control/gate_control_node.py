#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from visualization_msgs.msg import Marker
import serial


class ArduinoReader(Node):
    def __init__(self):
        super().__init__('arduino_reader_node')
        self.publisher_ = self.create_publisher(Int32, 'ultrasonic_distance', 10)
        self.marker_pub = self.create_publisher(Marker, 'visualization_marker', 10)

        self.ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)  # Update if needed
        self.timer = self.create_timer(0.5, self.read_from_serial)
        self.gate_open = False

    def read_from_serial(self):
        if self.ser.in_waiting:
            try:
                line = self.ser.readline().decode('utf-8').strip()
                distance = int(line)
                self.get_logger().info(f'Distance: {distance} cm')

                # Publish raw distance
                msg = Int32()
                msg.data = distance
                self.publisher_.publish(msg)

                # Decide gate state
                if distance < 15 and not self.gate_open:
                	self.gate_open=True
                elif distance > 20 and self.gate_open:
                	self.gate_open=False
                

                # Publish RViz markers
                self.publish_marker(distance, self.gate_open)

            except ValueError:
                self.get_logger().warn("Invalid data received")

    def publish_marker(self, distance, gate_open):
        # VEHICLE marker
        vehicle_marker = Marker()
        vehicle_marker.header.frame_id = "odom"
        vehicle_marker.header.stamp = self.get_clock().now().to_msg()
        vehicle_marker.ns = "vehicle"
        vehicle_marker.id = 0
        vehicle_marker.type = Marker.CUBE
        vehicle_marker.action = Marker.ADD
        vehicle_marker.scale.x = 0.3
        vehicle_marker.scale.y = 0.3
        vehicle_marker.scale.z = 0.3
        vehicle_marker.color.r = 0.0
        vehicle_marker.color.g = 0.0
        vehicle_marker.color.b = 1.0
        vehicle_marker.color.a = 1.0
        x_pos=max(0.1, min(float(distance)/100.0,3))
        vehicle_marker.pose.position.x = x_pos
        vehicle_marker.pose.position.y = 0.0
        vehicle_marker.pose.position.z = 0.15
        vehicle_marker.pose.orientation.w = 1.0

        # GATE marker
        gate_marker = Marker()
        gate_marker.header.frame_id = "odom"
        gate_marker.header.stamp = self.get_clock().now().to_msg()
        gate_marker.ns = "gate"
        gate_marker.id = 1
        gate_marker.type = Marker.CUBE
        gate_marker.action = Marker.ADD
        gate_marker.scale.x = 0.05
        gate_marker.scale.y = 1.0
        gate_marker.scale.z = 0.5
        gate_marker.color.r = 0.0
        gate_marker.color.g = 1.0 if gate_open else 0.0
        gate_marker.color.b = 0.0
        gate_marker.color.a = 1.0
        gate_marker.pose.position.x = 1.0  # Fixed gate position
        gate_marker.pose.position.y = 0.0
        gate_marker.pose.position.z = 0.25
        gate_marker.pose.orientation.w = 1.0

        # Publish both
        self.marker_pub.publish(vehicle_marker)
        self.marker_pub.publish(gate_marker)


def main(args=None):
    rclpy.init(args=args)
    node = ArduinoReader()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
