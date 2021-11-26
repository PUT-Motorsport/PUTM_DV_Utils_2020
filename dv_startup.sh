#!/bin/bash

sleep 1 && \
    cd /home/nuc/dv_ws && \
    source /opt/ros/melodic/setup.bash && \
    source devel/setup.bash && \
    sleep 100000 && \ # temporary to check if service works
    #v4l2-ctl -d /dev/video0 --set-ctrl low_latency_mode=1,gain=40,exposure_auto=0,exposure_time_absolute=1,brightness=-2,sharpness=20 && \
    #roslaunch dv mission.launch mission:=acc
