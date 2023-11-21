#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import sys, select, termios, tty

def getKey():
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

def inputKey():
    
    keystrock=input("")
    print (keystrock)
    return keystrock 

def keyOper():
    rospy.init_node("keyOperation", anonymous=False)
    message_pub = rospy.Publisher("turtle1/cmd_vel", Twist, queue_size=10)
    rate = rospy.Rate(10)  # Adjust the rate as needed

    while not rospy.is_shutdown():
        packet = Twist()
        #key = getKey()
        key=inputKey()
        print ( "key is " + key)

        if key == 'w':
            packet.linear.x = 2.0
        elif key == 's':
            packet.linear.x = -2.0
        else:
            packet.linear.x = 0.0

        if key == 'a':
            packet.angular.z = 2.0
        elif key == 'd':
            packet.angular.z = -2.0
        else:
            packet.angular.z = 0.0

        message_pub.publish(packet)
        rate.sleep()

if __name__ == '__main__':
    settings = termios.tcgetattr(sys.stdin)
    try:
        keyOper()
    except rospy.ROSInterruptException:
        pass
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
