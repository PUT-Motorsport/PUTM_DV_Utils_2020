#!/usr/bin/env python
import rospy
import time
import can
from std_msgs.msg import String


bustype = 'socketcan'
channel = 'vcan0'
# stopFlag = 0

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard: %s', data.data)
     #result = map(int, re.findall(r'\d+', data.data)) #find integers in string

    CANsend([data.data[0],data.data[1],0])



def CANsend(data):

    bus = can.interface.Bus(channel=channel, bustype=bustype)
    
    for i in range(10):

        msg = can.Message(arbitration_id=0x10, extended_id=False, is_remote_frame=False, is_error_frame=False, data=data)
        bus.send(msg)
        time.sleep(100)
    pass

def listener():



    rospy.init_node('CANsender', anonymous=True)

    rospy.Subscriber('flexbe2can', String, callback) #receiving messages from topic 'flexbe2can'

    rospy.spin()



if __name__ == '__main__':
    print("hi")
    listener()
