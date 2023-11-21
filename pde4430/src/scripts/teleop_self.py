#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from tkinter import Tk, Canvas, Frame, Button

class TeleopGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("TurtleSim Teleop")

        self.pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        self.twist_cmd = Twist()

        self.create_widgets()

    def create_widgets(self):
        frame = Frame(self.master)
        frame.pack()

        canvas = Canvas(frame, width=300, height=300)
        canvas.pack()

        # Define arrow buttons
        button_up = Button(frame, text="↑", command=self.move_turtle_up)
        button_up.bind("<ButtonRelease-1",self.move_turtle_stop)# Bind release even to stop button movement
        button_down = Button(frame, text="↓", command=lambda: self.move_turtle(-1, 0))
        button_left = Button(frame, text="←", command=lambda: self.move_turtle(0, 1))
        button_right = Button(frame, text="→", command=lambda: self.move_turtle(0, -1))

        # Place buttons on the grid
        button_up.grid(row=0, column=1)
        button_down.grid(row=2, column=1)
        button_left.grid(row=1, column=0)
        button_right.grid(row=1, column=2)

    def move_turtle_up(self):
        self.twist_cmd.linear.x=1
        self.twist_cmd.angular.z=0 
        print ("up is happening")   

    def move_turtle(self, linear, angular):
        self.twist_cmd.linear.x = linear
        self.twist_cmd.angular.z = angular
        self.pub.publish(self.twist_cmd)

    def move_turtle_stop(self ,event):
        self.twist_cmd.linear.x=0
        self.twist_cmd.linear.z=0
        self.pub.publish(self.twist_cmd)
        print ("Botton is relased")

if __name__ == "__main__":
    rospy.init_node('turtle_teleop')
    root = Tk()
    teleop_gui = TeleopGUI(root)
    rate=rospy.Rate(10) #10hz rate
    while not rospy.is_shutdown():
        root.update()
        rate.sleep()
        rospy.spin()
 