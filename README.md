# Swarm-Bot
- This is the **ROS** repository for multiple **omni drive** based robots used in a constrained indoor setting for navigating to efficently reach their respective goals. 
- We have designed a modular setting for a deploying both centralized and decentralized planning for traversing the terrain with other robots in the enviroment.   
- The major localization is done using **AprilTag Fiducial Markers** and used **odometry** for more accurate control. A total of 6 cameras were used in the setup to cover 7 ft * 7 ft .  
- The path-planning algorithm used is **Conflict-Based-Search (CBS)** using which a **Multi-Agent-Pickup-Delivery (MAPD)** Algorithm was developed to collect packages from the pickup stations and deliver them to the delivery chutes. 

For Hardware code visit this particular repo [Swarmbot-Hardware](https://github.com/Robotics-Club-IIT-BHU/Swarm-Bot-Hardware)  
<br> 
<br> 

<h2 align="center">Presenting Swarm-Bot<br></h2>
<br>
<p align="center"><img src="https://github.com/san2130/Multi-Agent-Pickup-Delivery/blob/master/SwarmBot.png" width="40%"/></p> 
<br>
<br>

## Setup guidelines 

```bash
cd catkin_ws/src
git clone git@github.com:Robotics-Club-IIT-BHU/Swarm-Bot.git
cd Swarm-Bot
./setup.sh
cd ../..
catkin build #or catkin_make
```


## Launching 

This would launch 4 Robots with its own namespaces for controlling them individually.

```bash
roslaunch dot_gazebo gazebo.launch ps:=ps1
roslaunch dot_gazebo gazebo.launch ps:=ps2
```
<br> 

<p align="center"><img src="https://github.com/san2130/Multi-Agent-Pickup-Delivery/blob/master/Simuation-_online-video-cutter.com_.gif" width="80%"></p>  
<br>
<br>
<br>

<h2 align="center">Hardware Results</h2>
<br> 

<p align="center"><img src="https://github.com/san2130/Multi-Agent-Pickup-Delivery/blob/master/TestRun%20(1).gif" width="70%"></p>
<br>
<br>

## Contributors
 * Somnath Kumar 
 * Varad Pandey
 * Harsh Mahesheka
 * Sandeepan Ghosh
 * Ankur Agrawal
 * Prateek
 * Surabhit Gupta
 * Vishwas Chepuri
 * Pranav Mittal
 * Aryaman Gupta
 * Dhruv Agarwal 
 * Vivek Agarwal
