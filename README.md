# PUT Motorsport Driverless Jetson Over IP configuration
Setup Jetson Xavier NX (or any other Jetson) to communicate with ROS master on another machine using network connection.

1. [Requirements](#requirements)
2. [Configuration](#configuration)
3. [Server startup](#startup)

## Requirements
* Jetson (tested on Xavier NX)
* ROS melodic (on both master and slave)
* Python

## Configuration

### Connect to Jetson

1. Install `minicom`
2. Change minicom settings:
```bash
minicom -s
```

2.A Change `Serial Port Setup` to following values
```bash
A - Serial Device           : /dev/ttyACM0  # Or the port of your connection
B - Lockfile Location       : /var/lock
C - Callin Program          :
D - Callout Program         :
E - Bps/Par/Bits            : 115200 8N1
F - Hardware Flow Control   : No
G - Software Flow Control   : No
```

2.B Change `Modem and dialing` options and remove **ALL** strings for options A-I and for option K
3. Save your configuration using `Save setup as dfl` option and select `Exit from Minicom`

### Setting up the network

1. Connect both machines to the switch

2. Start `minicom` to connect to Jetson with previous configuration
```bash
minicom
```

3. Set Jetson's IP Address for communication (**Make sure Jetson and host are in the same subnet!**)
```bash
ip addr add 192.168.1.2/24 dev eth0
```

4. Set the IP of the host machine (the ROS master)
```bash
ip addr add 192.168.1.1/24 dev eth0
# or if you use newer IP system
ip addr add 192.168.1.1/24 dev enp2s0
```

#### The above steps can be reproduced on Windows machine, where you need to set ip address as described [here](https://www.startech.com/en-eu/faq/networking-ip-change-win-10). Also, enp2s0 should be replaced with whichever port is connected to the switch!

### Connecting devices

1. On master, type the following
```
export ROS_MASTER_URI=http://192.168.1.1:11311
export ROS_IP=192.168.1.1
```

2. On Jetson, type the following
```
export ROS_MASTER_URI=http://192.168.1.1:11311
export ROS_IP=192.168.1.2
```

**Replace 192.168.1.1 with IP of your ROS Master and 192.168.1.2 of your ROS slave's IP**
#### You can automate both setting up the IP of your ROS master and ROS slave on linux by adding commands above to .bashrc file
Also, if you use Windows, use [this method](https://stackoverflow.com/questions/559816/how-to-export-and-import-environment-variables-in-windows) instead of `export`.

## Startup

Once the devices have the IP in the same subnet, you can test their connection:
```bash
ping 192.168.1.1
ping 192.168.1.2
# etc...
```

After that, you can start `roscore` on ROS Master and send data to it or retrieve from it using one of the ROS slave machines.

### Example setup (sending 'Hello world')
This repository contains `startup.launch`, `sender.py` and `receiver.py` used to represent basic communication between devices.

#### ROS Master
1. Create new catkin repository
```bash
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws
catkin_make
```

2. Create new package and add `startup.launch` and `receiver.py`
```bash
cd src
catkin_create_pkg example_package std_msgs rospy
mkdir -p ~/catkin_ws/src/example_package/src/scripts
mkdir -p ~/catkin_ws/src/example_package/src/launch
cp startup.launch ~/catkin_ws/src/example_package/src/launch
cp receiver.py ~/catkin_ws/src/example_package/src/launch
cd ~/catkin_ws
catkin_make
# Don't forget to source it!
source ~/catkin_ws/devel/setup.bash
```

3. Start the server using launch file
```bash
roslaunch example_package startup.launch
```

#### ROS Slave
1. Add `sender.py` to your current directory
```bash
cp sender.py .
```

2. Start it using python
```bash
python sender.py
```

Now you should be able to see the ROS slave send 'Hello world (TIME)' to the ROS master.
