#!/usr/bin/env python

import rospy
from add_int_service.srv import *

def call_service():
    x = 0
    rate = rospy.Rate(1) # 1hz
    while not rospy.is_shutdown():
        x = add_two_ints(x, 1).sum
        rospy.loginfo("sum returned : %s" %x)
        rate.sleep()

if __name__ == "__main__":
    rospy.init_node('call_service', anonymous=True)
    rospy.wait_for_service('add_two_ints')
    try:
        add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts)
        call_service()
    except rospy.ROSInterruptException:
        pass
