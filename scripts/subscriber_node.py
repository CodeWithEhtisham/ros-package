#! /usr/bin/python3

import rospy 
from  std_msgs.msg import String
from testing.msg import mymsg

def callback(data):
    rospy.loginfo("%s: , %f: ,%f: ",data.message,data.x,data.y)

def listener():
    rospy.init_node('my_subscriber_node',anonymous=True)
    rospy.Subscriber('my_publisher',mymsg,callback)
    rospy.spin()

if __name__=='__main__':
    try:
        listener()
    except rospy.exceptions.ROSInterruptException:
        pass