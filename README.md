# PUT Motorsport Driverless ROS2CAN Utilities

Package which provides ROS <-> CAN communication (both ways)


1. [Requirements](#requirements)
2. [Configuration](#configuration)


## Requirements
- Ubuntu 18.04
- ROS Melodic
- DV Workspace (from DV recruitment task)


## Configuration

### Import can library and create a virtual CAN
```bash
modprobe can_dev
modprobe can_raw
modprobe vcan
sudo ip link add dev vcan0 type vcan
sudo ip link set up vcan0
```

### Make ROS workspace and get recruitment task repository
```bash
cd ~/dv_ws/src
git clone -b can https://github.com/PUT-Motorsport/PUTM_DV_utils_2020.git 
```

### Build workspace
```bash
cd ~/dv_ws
catkin_make
source devel/setup.bash
roscore
```

### Run node (another terminal)
```bash
cd ~/dv_ws
source devel/setup.bash
rosrun ros2can CANsender.py
```