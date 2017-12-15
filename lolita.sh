#!/bin/bash
echo "source environment.sh"
source environment.sh
echo "source set_ros_master.sh duckie"
source set_ros_master.sh duckie
echo "source set_vehicle_name.sh duckie"
source set_vehicle_name.sh duckie
echo "roslaunch duckietown_demos lane_following.launch veh:=duckie line_detector_param_file_name:=universal verbose:=true"
roslaunch duckietown_demos lane_following.launch veh:=duckie line_detector_param_file_name:=universal verbose:=true


