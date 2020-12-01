#!/usr/bin/env python
import rospy
import time
import can
from std_msgs.msg import String


bustype = 'socketcan'
channel = 'vcan0'
#counter = 0

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard: %s', data.data)



def CANsend():

    bus = can.interface.Bus(channel=channel, bustype=bustype)
    for i in range(100):

        
        msg = can.Message(arbitration_id=0x0A, extended_id=False, data=[10, i, 0])
        bus.send(msg)
        msg = can.Message(arbitration_id=0x0B, extended_id=False, is_remote_frame=False, is_error_frame=False, data=[10, i, 0, 1, 13, 1])
        bus.send(msg)

    time.sleep(1)
    


    pass

def listener():

    

    rospy.init_node('CANsender', anonymous=True)

    rospy.Subscriber('ROSnode', String, callback) #receiving messages from topic 'ROSnode'

    rate = rospy.Rate(2) # Hz

    while not rospy.is_shutdown():
            CANsend()
            rate.sleep()


    rospy.spin()



if __name__ == '__main__':
    print("hi")
    listener()
