#!/usr/bin/env python

import sys
import rospy
from add_int_service.srv import *
from std_msgs.msg import Int64

x=0
y=1
def add_two_ints_client(x, y):
    rospy.wait_for_service('add_two_ints')
    try:
        add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts)
        resp1 = add_two_ints(x, y)
        return resp1.sum
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e


def call_service():
    global x,y
    rospy.init_node('call_service', anonymous=True)
    pub = rospy.Publisher('chatter', Int64, queue_size=10)
    rate = rospy.Rate(1) # 10hz
    while not rospy.is_shutdown():
        x,y= y, add_two_ints_client(x, y)
        print y
        pub.publish(y)
        rate.sleep()

if __name__ == "__main__":
    try:
        call_service()
    except rospy.ROSInterruptException:
        pass
