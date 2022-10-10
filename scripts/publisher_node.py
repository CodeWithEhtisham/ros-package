#!/usr/bin/python3

from itertools import count
import rospy
from std_msgs.msg import String
from testing.msg import mymsg 

def ros_talker():
    pub = rospy.Publisher('my_publisher',mymsg,queue_size=10)

    rospy.init_node('my_publisher_node',anonymous=True)

    rate=rospy.Rate(10)

    rospy.loginfo("Publisher node started")
    counter=1
    while not rospy.is_shutdown():
        msg=mymsg()
        msg.message=f"{counter} message"
        msg.x=counter
        msg.y=counter
        pub.publish(msg)
        rate.sleep()
        counter+=1


if __name__=='__main__':
    try:
        ros_talker()
    except rospy.exceptions.ROSInterruptException:
        pass