#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

class MoveTurtleToPosition:
    def __init__(self, turtle_name):
        rospy.init_node('move_turtle_to_position', anonymous=True)
        self.velocity_publisher = rospy.Publisher(f'/{turtle_name}/cmd_vel', Twist, queue_size=10)
        self.pose_subscriber = rospy.Subscriber(f'/{turtle_name}/pose', Pose, self.update_pose)
        self.pose = Pose()
        self.rate = rospy.Rate(10)  # Rate in Hz
        self.turtle_name = turtle_name

    def update_pose(self, data):
        self.pose = data

    def move_to_position(self, target_x, target_y):
        vel_msg = Twist()

        while True:
            # Calculate relative distance to move to the target position
            distance = ((target_x - self.pose.x) ** 2 + (target_y - self.pose.y) ** 2) ** 0.5

            # Set linear and angular velocities to move towards the target
            vel_msg.linear.x = 1.0 * distance  # Adjust the speed as needed
            vel_msg.angular.z = 4.0 * (self.calculate_angle(target_x, target_y) - self.pose.theta)

            self.velocity_publisher.publish(vel_msg)
            self.rate.sleep()

            # Break the loop when the turtle reaches close to the target position
            if distance < 0.1:
                break

        # Stop the turtle once it reaches the target position
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)

    def calculate_angle(self, target_x, target_y):
        return math.atan2(target_y - self.pose.y, target_x - self.pose.x)

if __name__ == '__main__':
    try:
        turtle1 = MoveTurtleToPosition('turtle1')  # Create instance for the first turtle
        turtle2 = MoveTurtleToPosition('turtle2')  # Create instance for the second turtle
        turtle3=MoveTurtleToPosition('turtle3')

        # Move the first turtle to position (1, 10)
        turtle1.move_to_position(1, 10)

        if round(turtle1.pose.x) == 1 and round(turtle1.pose.y) == 10:
            print("Turtle1 reached initial position (1, 10)")

            # Move the second turtle to position (9, 1)
            turtle2.move_to_position(9, 1)
            turtle3.move_to_position(8,2)

            if round(turtle2.pose.x) == 9 and round(turtle2.pose.y) == 1:
                print("Turtle2 reached position (9, 1)")

        else:
            print("Turtle1 didn't reach the initial position")
            
    except rospy.ROSInterruptException:
        pass
