#!/usr/bin/python
import sys
import fileinput

output = "Couldn't find ros source..."

for line in fileinput.input('/home/jake/.bashrc', inplace=False):
    if(line.find('source /opt/ros/indigo/setup.bash') != -1):
        output = "ROS Source: indigo"
    elif(line.find('source /opt/ros/jade/setup.bash') != -1):
        output = "ROS Source: jade"

print output