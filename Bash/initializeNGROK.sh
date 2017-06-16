#!/bin/bash
echo "Starting NGROK"
cd /home/pi/NGrokServer/
./ngrok tcp --remote-addr 1.tcp.ngrok.io:29161 22
#@reboot sh /home/pi/Desktop/runNGR.sh