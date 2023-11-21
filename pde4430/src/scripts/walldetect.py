#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose

def callback(data):
    if data.x>10 or data.x<1 or data.y>10 or data.y<1:
        print("crash detected")
    else :
        print ("Good to go")
        
def Listener():
    rospy.init_node("wall_detector",anonymous=False)
    rospy.Subscriber("/turtle1/pose",Pose,callback)

if __name__=="__main__":
    Listener()
    rospy.spin()