#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

class CleaningBot:
    def __init__(self):
        rospy.init_node('cleaning_bot', anonymous=True)
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        self.pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, self.update_pose)
        self.pose = Pose()
        self.rate = rospy.Rate(1)
        self.prev_positions = []  # List to store previous positions

    def update_pose(self, data):
        self.pose = data
        self.pose.x = round(self.pose.x, 4)
        self.pose.y = round(self.pose.y, 4)

    def move_to_position(self, x, y):
        vel_msg = Twist()

        while abs(self.pose.x - x) > 0.1:
            vel_msg.linear.x = 2* math.sqrt((x - self.pose.x) ** 2 + (y - self.pose.y) ** 2)
            vel_msg.angular.z = 4 * (math.atan2(y - self.pose.y, x - self.pose.x) - self.pose.theta)

            self.velocity_publisher.publish(vel_msg)
            self.rate.sleep()

        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)

    def store_position(self):
        # Store the current position
        self.prev_positions.append((self.pose.x, self.pose.y))

    def return_to_previous_positions(self):
        for position in reversed(self.prev_positions):
            self.move_to_position(position[0], position[1])

    def clean_x_direction(self):
        for i in range(1, 10):
            self.move_to_position(i, 0)
            self.store_position()

            self.move_to_position(i, 9)
            self.store_position()

    def clean_y_positions(self):
        for i in range(1, 10):
            self.move_to_position(1, i)
            self.store_position()

            self.clean_x_direction()

    def clean_cycle(self):
        self.move_to_position(1, 0)
        self.store_position()

        self.clean_y_positions()

        self.return_to_previous_positions()

if __name__ == '__main__':
    try:
        bot = CleaningBot()
        #bot.clean_cycle()
        bot.clean_x_direction()
        bot.clean_y_positions()
    except rospy.ROSInterruptException:
        pass
