#!/usr/bin/env python3
import rospy
import serial
from sensor_msgs.msg import LaserScan

LIDAR_PORT = "/dev/ttyUSB0"
LIDAR_BAUDRATE = 115200

def read_lidar():
    """Reads LIDAR data from serial port"""
    ser = serial.Serial(LIDAR_PORT, LIDAR_BAUDRATE)
    pub = rospy.Publisher("/scan", LaserScan, queue_size=10)
    rospy.init_node("lidar_processing", anonymous=True)
    
    while not rospy.is_shutdown():
        if ser.in_waiting > 0:
            distance = ser.readline().decode().strip()
            scan_data = LaserScan()
            scan_data.ranges.append(float(distance))
            pub.publish(scan_data)
            rospy.loginfo(f"LIDAR Distance: {distance} cm")

if __name__ == "__main__":
    try:
        read_lidar()
    except rospy.ROSInterruptException:
        pass
