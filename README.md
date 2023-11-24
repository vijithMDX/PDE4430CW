# PDE4430CW
# TurtleBot Demo for PDE4430 Coursework

This repository contains a demonstration related to the PDE4430 coursework, showcasing the utilization of TurtleBot within the context of the course.

## Overview

The TurtleBot demo provides a Graphical User Interface (GUI) window that integrates keyboard functionality for controlling the TurtleSim. The GUI window allows for easy control and interaction with multiple TurtleBots. Here are the functionalities provided by the GUI:

- **Keyboard Controls:**
  - Use `W` or `Up Arrow` to move the TurtleBot forward.
  - Use `S` or `Down Arrow` to move the TurtleBot backward.
  - Use `A` or `Left Arrow` to rotate the TurtleBot anti-clockwise.
  - Use `D` or `Right Arrow` to rotate the TurtleBot clockwise.
  - Press `R` for acceleration up to 10 units.
  - Press `F` for deceleration.

## Usage

To run the TurtleBot demo:

1. **Launch the TurtleBot Environment:**
   - Run the command `roslaunch pde4430 multiBot.launch` to launch the environment.
   - Three TurtleBots and the GUI window will appear.
     

2. **Interacting with the GUI:**
   - **Moving Bots:** Click on each TurtleBot button to select and move individual bots in the GUI window.
   - **Setting Goal Positions:** Enter the desired goal position in the provided text box and click "Move to Goal" to move each bot to the specified position.
   - **Wall Detection:** A wall detection program runs in the background. It will detect and provide alerts if a bot touches a wall.
   - **Cleaning Operation:** Start cleaning operations for individual or multiple bots. Individual bot cleaning performs grid behavior(choose the turtle to start), while multiple cleaning performs spiral behavior.
   - **Returning Home:** Use the option to move the bot to its home position.

3. **Note:** If you encounter difficulties viewing more than one TurtleBot, relaunch the launch file.

## Author

- **Author:** Vijith Viswan | M00986814
- **Course:** PDE4430


