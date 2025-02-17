#!/usr/bin/env python3
import rospy
import paramiko
from std_msgs.msg import String

SSH_HOST = "192.168.X.X"
SSH_USER = "pi"
SSH_PASS = "raspberry"

def send_command(command):
    """Send motor control commands via SSH."""
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(SSH_HOST, username=SSH_USER, password=SSH_PASS)
        stdin, stdout, stderr = client.exec_command(f"python3 motor_control.py {command}")
        rospy.loginfo(stdout.read().decode().strip())
        client.close()
    except Exception as e:
        rospy.logerr(f"SSH Error: {e}")

def command_callback(msg):
    """Receive movement commands from ROS topics."""
    if msg.data in ["forward", "backward", "stop"]:
        send_command(msg.data)

def main():
    rospy.init_node("ugv_controller", anonymous=True)
    rospy.Subscriber("/ugv/movement", String, command_callback)
    rospy.spin()

if __name__ == "__main__":
    main()
