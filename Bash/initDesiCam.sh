#!/bin/bash
echo "Starting NGROK DESICAM" >> /home/pi/Desktop/SentinelGreen/Logs/DesiCam.txt
cd /home/pi/NGrokServer/
./ngrok http -subdomain=desicam 80