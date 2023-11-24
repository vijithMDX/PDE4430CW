#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose

class wall_detector:
    def __init__(self,turtle_name):
        self.turtle=turtle_name
        self.sub= rospy.Subscriber(f"/{self.turtle}/pose",Pose,self.callback)
        #Listener(self.turtle_name)


    def callback(self,data):
        if data.x>10 or data.x<1 or data.y>10 or data.y<1:
            print("crash detected")
       
            
    
        #rospy.init_node("wall_detector",anonymous=False)
        
'''
if __name__=="__main__":
    Listener()
    rospy.spin()
'''