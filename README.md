# Swarm-Bot
This is the ROS repository for multiple **omni drive** based robots used in a constrained indoor setting for navigating to efficently reach their respective goals. 
We have designed a modular setting for a deploying both centralized and decentralized planning for traversing the terrain with other robts in the enviroment. The major locatization is done using Apriltags and used odometry for more accurate control.

For Hardware code visit this particular repo [Swarmbot-Hardware](https://github.com/Robotics-Club-IIT-BHU/Swarm-Bot-Hardware)

# Setup guidelines 

```bash
cd catkin_ws/src
git clone git@github.com:Robotics-Club-IIT-BHU/Swarm-Bot.git
cd Swarm-Bot
./setup.sh
cd ../..
catkin build #or catkin_make
```


# Launching 

This would launch 4 Robots with its own namespaces for controlling them individually.

```bash
roslaunch dot_gazebo gazebo.launch ps:=ps1
roslaunch dot_gazebo gazebo.launch ps:=ps2
```

# Contributors
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
