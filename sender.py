#!/usr/bin/env python
import rospy
from std_msgs.msg import String

# Send 'hello world' + time to topic '/test' with 10Hz frequency

def talker():
    pub = rospy.Publisher('/test', String, queue_size=10)
    rospy.init_node('sender', anonymous=True)
    rate = rospy.Rate(10) # 10 Hz
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        pub.publish(hello_str)
        rate.sleep()

if __name__ == "__main__":
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
