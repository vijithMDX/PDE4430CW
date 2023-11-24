#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

class MoveTurtleToPosition:
    def __init__(self):
        rospy.init_node('move_turtle_to_position', anonymous=True)
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        self.pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, self.update_pose)
        self.pose = Pose()
        self.rate = rospy.Rate(4)  # Rate in Hz

    def update_pose(self, data):
        self.pose = data
    def clean_x_direction(self):
        y_goal=1
        for _ in range (1,9):
            for x_goal in range (1,9):
                self.go_to_goal(x_goal,y_goal)
                print("cleaning in  x direction")
            y_goal+=2

    def gridClean(self):
        self.move_to_position(1,1)
        self.move_to_position(1,9)
        self.move_to_position(9,9)
        self.move_to_position(1,9)


    def spiralClean(self):
        vel_msg = Twist()
        loop_rate = rospy.Rate(1)
        wk = 4
        rk = 0
        currentTurtlesimPose=Pose()
    
        while True:
            rk=rk+1
            vel_msg.linear.x =rk
            vel_msg.linear.y =0
            vel_msg.linear.z =0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z =wk
            self.velocity_publisher.publish(vel_msg)
            loop_rate.sleep()
            print(f"{self.pose.x} x and y{self.pose.y}")
            if ((round(self.pose.x)>=10) and (round(self.pose.y)>=9)):
                break
    
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)

    def move_to_position(self, target_x, target_y):
        vel_msg = Twist()

        while True:
            # Calculate relative distance to move to the target position
            distance = math.sqrt((target_x - self.pose.x) ** 2 + (target_y - self.pose.y) ** 2)

            # Set linear and angular velocities to move towards the target
            vel_msg.linear.x = 1.0 * distance  # Adjust the speed as needed
            vel_msg.angular.z = 4.0* (math.atan2(target_y - self.pose.y, target_x - self.pose.x) - self.pose.theta)

            self.velocity_publisher.publish(vel_msg)
            #self.rate=rospy.Rate(4)

            # Calculate the remaining distance to the target position
            remaining_distance = math.sqrt((target_x - self.pose.x) ** 2 + (target_y - self.pose.y) ** 2)

            # Break the loop when the turtle is very close to the target position
            if remaining_distance < 0.10 or (target_x==round(self.pose.x) and target_y==round(self.pose.y)) :
                print("reached pos")
                break
            else: 
                print("Loop overrun")
                print(f"Cleaning pos ({target_x}, {target_y})")

                    # Print the final position for debugging
                print(f"Current position: x = {round(self.pose.x)}, y = {round(self.pose.y)}")
            rospy.Rate(10)

        # Stop the turtle once it reaches the target position
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)

    

   
    

if __name__ == '__main__':
    try:
        move_turtle = MoveTurtleToPosition()
        
        print("Starting turtle")

        # Move to the initial position (1, 10)
        move_turtle.move_to_position(1, 10)
       
        
        move_turtle.spiralClean()

        if round(move_turtle.pose.x) == 1 and round(move_turtle.pose.y) == 10:
            print("Reached initial position (1, 10)")

           

        else:
            print(move_turtle.pose.x, "", move_turtle.pose.y)
            print("Didn't reach the initial position")
            move_turtle.move_to_position(1, 10)
            
    except rospy.ROSInterruptException:
        pass
