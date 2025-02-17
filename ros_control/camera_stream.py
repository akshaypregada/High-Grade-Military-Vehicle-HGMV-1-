#!/usr/bin/env python3
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

ESP32_STREAM_URL = "http://192.168.X.X:81/stream"

def stream_camera():
    """Captures and publishes ESP32 camera feed."""
    rospy.init_node("camera_stream", anonymous=True)
    pub = rospy.Publisher("/camera/image_raw", Image, queue_size=10)
    bridge = CvBridge()
    
    cap = cv2.VideoCapture(ESP32_STREAM_URL)
    
    while not rospy.is_shutdown():
        ret, frame = cap.read()
        if ret:
            pub.publish(bridge.cv2_to_imgmsg(frame, "bgr8"))
            cv2.imshow("UGV Camera Feed", frame)
        
        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    try:
        stream_camera()
    except rospy.ROSInterruptException:
        pass
