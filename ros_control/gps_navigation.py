#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import NavSatFix

TARGET_LAT = 37.7749
TARGET_LONG = -122.4194

def callback(data):
    lat = data.latitude
    long = data.longitude
    rospy.loginfo(f"Current Position: {lat}, {long}")

    if abs(lat - TARGET_LAT) < 0.0001 and abs(long - TARGET_LONG) < 0.0001:
        rospy.loginfo("Target Reached!")
        return

def main():
    rospy.init_node("gps_navigation")
    rospy.Subscriber("/fix", NavSatFix, callback)
    rospy.spin()

if __name__ == "__main__":
    main()
