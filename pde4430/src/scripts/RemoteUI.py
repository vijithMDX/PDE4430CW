#!/usr/bin/env python3

#auther vijith
#Teleoperation UI and Keyboard interface . for multilple turtlebot ,
#Currently integrated 3 bot
import rospy
from geometry_msgs.msg import Twist
from tkinter import Tk, Canvas, Frame, Button,Label



class TeleopGUI:
    
    def __init__(self, master):
        self.x=1
        self.main = master
        self.main.title("TurtleSim Teleop")
        self.turtle_name="turtle1"

        
        self.twist_cmd = Twist()

        self.create_widgets()
        self.setup_aeroKeyOperation()
        self.printHeader()
    def printHeader(self):
        print ("             ")
        print("\n hello folks")
        print("..... This is a teleopertion insturction of TurtleBot....")
        print("\n .. use ^ aero key / w for forward motion ...")
        print ("\n .. Use down aero /s for backward motion")
        print("\n .. use >  aero key / d for rotating right")
        print("\n ..use < / a for rotating left..")
        print(" \n..use r key for accel..")
        print("\n ..f key for decel..")
        

    def setup_aeroKeyOperation(self):
        #defining keyboard operation.
        '''
        up arrow or w for going up
        down arrow or s for going down
        left arrow or a for rotating left
        right arrow or d for rotiatin right

        + buttn for speed up
        - button for speed down

        '''
        
        self.main.bind('<r>',self.speedUp)
        self.main.bind('<f>',self.speedDown)
        

        self.main.bind('<Up>',lambda event,motion=(1,0):self.move_turtle_start(event,motion)) ,self.main.bind('<w>',lambda event,motion=(1,0):self.move_turtle_start(event,motion))   

        self.main.bind('<Down>',lambda event,motion=(-1,0):self.move_turtle_start(event,motion)),self.main.bind('<s>',lambda event,motion=(-1,0):self.move_turtle_start(event,motion)),

        self.main.bind('<Left>',lambda event,motion=(0,1):self.move_turtle_start(event,motion)),self.main.bind('<a>',lambda event,motion=(0,1):self.move_turtle_start(event,motion))

        self.main.bind('<Right>',lambda event,motion=(0,-1):self.move_turtle_start(event,motion)),self.main.bind('<d>',lambda event,motion=(0,-1):self.move_turtle_start(event,motion))
    
    
    def speedUp(self,event):
        
        if (self.x<10):
            self.x += 1
            
        else:self.x=1

        print (f"acceleration : {self.x}")
        
        
    def speedDown(self,event):
        
        if (self.x >1):
            self.x-=1
        else :
            self.x=1
        print (f"acceleration : {self.x}")
    
    


    def create_widgets(self):
        frame = Frame(self.main)
        frame.pack()

        canvas = Canvas(frame, width=300, height=300)

        # Creating arrow buttons
        self.button_up = Button(frame, text="↑")
        self.button_down = Button(frame, text="↓")
        self.button_left = Button(frame, text="←")
        self.button_right = Button(frame, text="→")
        self.header_label=Label(frame,text="Teleoperation virtual keyboard")
        self.accel=Button(frame,text="Acl")
        self.decele=Button(frame,text="Dec")

        #creating turtle selection button
        
        self.choose_turtle1=Button(frame,text="Turtle 1")
        self.choose_turtle2=Button(frame,text="Turtle 2")
        self.choose_turtle3=Button(frame,text="Turtle 3")

        # here all binding fuction for press and release events for each button
        self.button_up.bind("<ButtonPress-1>", lambda event, motion=(1, 0): self.move_turtle_start(event, motion))
        self.button_down.bind("<ButtonPress-1>", lambda event, motion=(-1, 0): self.move_turtle_start(event, motion))
        self.button_left.bind("<ButtonPress-1>", lambda event, motion=(0, 1): self.move_turtle_start(event, motion))
        self.button_right.bind("<ButtonPress-1>", lambda event, motion=(0, -1): self.move_turtle_start(event, motion))
        self.accel.bind("<ButtonPress-1>",lambda event:self.speedUp(event))
        self.decele.bind("<ButtonPress-1>",lambda event:self.speedDown(event))

        # Binding for choosing turtle
        self.choose_turtle1.bind("<ButtonPress-1>",lambda event:self.turtle1selected(event))
        self.choose_turtle2.bind("<ButtonPress-1>",lambda event:self.turtle_2_selected(event))
        self.choose_turtle3.bind("<ButtonPress-1>",lambda event:self.turtle_3_selected(event))
        
        '''
        self.button_up.bind("<ButtonRelease-1>", self.move_turtle_stop)
        self.button_down.bind("<ButtonRelease-1>", self.move_turtle_stop)
        self.button_left.bind("<ButtonRelease-1>", self.move_turtle_stop)
        self.button_right.bind("<ButtonRelease-1>", self.move_turtle_stop)
        '''
        self.header_label.grid(row=0,column=1)
        self.button_up.grid(row=1, column=1)
        self.button_down.grid(row=2, column=1)
        self.button_left.grid(row=1, column=0)
        self.button_right.grid(row=1, column=2)
        self.accel.grid(row=3,column=0)
        self.decele.grid(row=3,column=2)
        
        self.choose_turtle1.grid(row=4,column=0)
        self.choose_turtle2.grid(row=4,column=1)
        self.choose_turtle3.grid(row=4,column=2)
    
    
    def turtle1selected(self,event):
        self.turtle_name="turtle1"
    def turtle_2_selected(self,event):
        self.turtle_name="turtle2"
    def turtle_3_selected(self,event):
        self.turtle_name="turtle3"
    
    
    def move_turtle_start(self, event, motion):
        motion=self.x*motion[0],motion[1]
        self.twist_cmd.linear.x, self.twist_cmd.angular.z =motion
        self.sendVel_val(self.twist_cmd)

        print(f"x,z value is {motion}") 

    def move_turtle_stop(self, event):
        self.twist_cmd.linear.x = 0
        self.twist_cmd.angular.z = 0

        self.sendVel_val(self.twist_cmd)
        
    def sendVel_val(self,twist_msg):
        pub=rospy.Publisher(f'/{self.turtle_name}/cmd_vel', Twist, queue_size=10)
        pub.publish(self.twist_cmd)


if __name__ == "__main__":
    rospy.init_node('turtle_teleop')
    root = Tk()
    teleop_gui = TeleopGUI(root)
    
    
    root.mainloop()
