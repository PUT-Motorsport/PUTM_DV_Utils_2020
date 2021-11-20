#!/usr/bin/env python
import rospy
from std_msgs.msg import String

# Script to listen to topic \test and print every message sent there on screen

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + " heard %s", data.data)

def listener():
    rospy.init_node('receiver', anonymous=True)
    rospy.Subscriber("\test", String, callback)
    rospy.spin()

if __name__ == "__main__":
    listener()
