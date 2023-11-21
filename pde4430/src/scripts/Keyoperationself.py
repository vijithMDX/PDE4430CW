#!/usr/bin/env/python3
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
        canvas.grid(row=0, column=0, columnspan=3)

        # Set up buttons for continuous motion
        button_up = Button(frame, text="↑", command=self.move_turtle_up_start, repeatdelay=500, repeatinterval=100)
        button_down = Button(frame, text="↓", command=self.move_turtle_down_start, repeatdelay=500, repeatinterval=100)
        button_left = Button(frame, text="←", command=self.move_turtle_left_start, repeatdelay=500, repeatinterval=100)
        button_right = Button(frame, text="→", command=self.move_turtle_right_start, repeatdelay=500, repeatinterval=100)

        # Set up buttons for stopping motion
        button_stop = Button(frame, text="Stop", command=self.stop_turtle)

        button_up.grid(row=1, column=1)
        button_down.grid(row=2, column=1)
        button_left.grid(row=1, column=0)
        button_right.grid(row=1, column=2)
        button_stop.grid(row=2, column=2)

        # Set up button release events
        self.master.bind("<KeyRelease-Up>", lambda event: self.move_turtle_stop())
        self.master.bind("<KeyRelease-Down>", lambda event: self.move_turtle_stop())
        self.master.bind("<KeyRelease-Left>", lambda event: self.move_turtle_stop())
        self.master.bind("<KeyRelease-Right>", lambda event: self.move_turtle_stop())

    def move_turtle_up_start(self):
        self.move_turtle_start(1, 0)

    def move_turtle_down_start(self):
        self.move_turtle_start(-1, 0)

    def move_turtle_left_start(self):
        self.move_turtle_start(0, 1)

    def move_turtle_right_start(self):
        self.move_turtle_start(0, -1)

    def move_turtle_start(self, linear, angular):
        self.twist_cmd.linear.x = linear
        self.twist_cmd.angular.z = angular
        self.pub.publish(self.twist_cmd)

    def move_turtle_stop(self):
        self.twist_cmd.linear.x = 0
        self.twist_cmd.angular.z = 0
        self.pub.publish(self.twist_cmd)

    def stop_turtle(self):
        self.move_turtle_stop()

def main():
    rospy.init_node('turtle_teleop')
    root = Tk()
    teleop_gui = TeleopGUI(root)

    root.mainloop()

if __name__ == "__main__":
    main()
