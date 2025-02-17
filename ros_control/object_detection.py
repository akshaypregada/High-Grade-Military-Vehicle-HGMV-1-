#!/usr/bin/env python3
import rospy
import cv2
import torch
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # Pretrained model
bridge = CvBridge()

def callback(img_msg):
    frame = bridge.imgmsg_to_cv2(img_msg, "bgr8")
    results = model(frame)

    for result in results:
        frame = result.plot()  # Overlay bounding boxes

    cv2.imshow("Object Detection", frame)
    cv2.waitKey(1)

def main():
    rospy.init_node("object_detection")
    rospy.Subscriber("/camera/image_raw", Image, callback)
    rospy.spin()

if __name__ == "__main__":
    main()
