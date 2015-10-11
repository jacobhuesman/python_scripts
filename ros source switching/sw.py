#!/usr/bin/python
import sys
import fileinput

output = "Couldn't find ros source..."

for line in fileinput.input('/home/jake/.bashrc', inplace=True):
    if(line.find('source /opt/ros/indigo/setup.bash') != -1):
        sys.stdout.write(line.replace('source /opt/ros/indigo/setup.bash', 'source /opt/ros/jade/setup.bash'))
        output = "Replaced indigo with jade."
    elif(line.find('source /opt/ros/jade/setup.bash') != -1):
        sys.stdout.write(line.replace('source /opt/ros/jade/setup.bash', 'source /opt/ros/indigo/setup.bash'))
        output = "Replaced jade with indigo."
    else:
        sys.stdout.write(line)

print output