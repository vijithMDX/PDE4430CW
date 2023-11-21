#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import pygame

def keyOper():
    rospy.init_node("keyboard_control_node", anonymous=False)
    message_pub = rospy.Publisher("turtle1/cmd_vel", Twist, queue_size=10)
    rate = rospy.Rate(10)  # Adjust the rate as needed

    pygame.init()
    screen = pygame.display.set_mode((100, 100))

    while not rospy.is_shutdown():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rospy.signal_shutdown("Quit event detected")
            elif event.type == pygame.KEYDOWN:
                packet = Twist()

                if event.key == pygame.K_w:
                    print ("pressed up")
                    packet.linear.x = 2.0
                elif event.key == pygame.K_s:
                     print ("pressed down")
                     packet.linear.x = -2.0
                elif event.key == pygame.K_a:
                    packet.angular.z = 2.0
                elif event.key == pygame.K_d:
                    packet.angular.z = -2.0

                elif event.key==pygame.K_UP:
                    print ("pressed up")
                    packet.linear.x = 2.0
                elif event.key ==pygame.K_DOWN:
                    print ("pressed down")
                    packet.linear.x=-2.0
                elif event.key== pygame.K_LEFT:
                    packet.angular.z=2.0
                    print ("pressed left")
                elif event.key==pygame.K_RIGHT:
                    print ("pressed right")
                    packet.angular.z=-2.0
                message_pub.publish(packet)

        rate.sleep()

if __name__ == '__main__':
    try:
        keyOper()
    except rospy.ROSInterruptException:
        pass
    finally:
        pygame.quit()
