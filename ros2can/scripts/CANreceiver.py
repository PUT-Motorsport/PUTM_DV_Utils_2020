#!/usr/bin/env python

import time
import can

import rospy
from std_msgs.msg import String


#receiving messages in CAN and send them to ROSnode
def talker():
    can_interface = 'vcan0'
    bus = can.interface.Bus(can_interface, bustype='socketcan')
    pub = rospy.Publisher('ROSnode', String, queue_size=10) #sending messages to topic 'ROSnode'
    rospy.init_node('talker', anonymous=True) 
    rate = rospy.Rate(1) # 1hz
    while not rospy.is_shutdown():
        message = bus.recv() #listening to CAN
        hello_str = "CAN SAYS: " + str(message)
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        print("hi")
        talker()
    except rospy.ROSInterruptException:
        pass
