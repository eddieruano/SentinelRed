# -*- coding: utf-8 -*-
# @Author: Eddie Ruano
# @Date:   2017-06-13 11:11:04
# @Last Modified by:   Eddie Ruano
# @Last Modified time: 2017-06-13 17:29:38
"""
    MainController contains all threading control logic
"""
import logging
import threading
import time
import sys
import os
################################### PATHS #####################################
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import Sensors.HCSR04 as HCSR04

# Localities
#from .Sensors import HCSR04

""" Initialization of Central Logger """
# Top Vars
LogLevel = logging.DEBUG        ## Change this later
LogLocation = "mainLog.txt"
#-------S8Proto
# Create Instance of Logger
Houston = logging.getLogger(__name__)
# Setting Logging Level --Change from Debug later
Houston.setLevel(level=LogLevel)
# Set up Format Protocol --> Type of Msg, Name of Module, Time, PayloadMessage
HouForm = logging.Formatter('%(levelname)s:%(name)s:%(asctime)s:%(message)s')
# Set up File Handler + Add level + add formatter
HouFile = logging.FileHandler(LogLocation)
HouFile.setLevel(LogLevel)
HouFile.setFormatter(HouForm)
# Set up Stream Handler + level + format
HouStream = logging.StreamHandler()
HouStream.setLevel(LogLevel)
HouStream.setFormatter(HouForm)
# Add all handlers to instance of Handler
Houston.addHandler(HouStream)
Houston.addHandler(HouFile)
Houston.info("Logger has been created.")
""" Initialization of Global Variables """
Voyager1 = HCSR04.HCSR04("Voyager1", 17, 4)

class MainController(object):
    global Houston, Voyager1
    Distance = 0.0
    Status = True
    
    def __init__(self):
        pass
    def mainLoop(self):
        # Create the threads
        dist = threading.Thread(name='ThreadV1', target=self.threadSensorRead, args=(Houston, self.Distance))
        check = threading.Thread(name='CheckC', target=self.threadControlRead, args=(Houston, self.Status))
        # Start the threads
        dist.start()
        check.start()
        while True:
            print("In the loop")
            print("Dist: ")
            print(self.Distance)
            print("Status: ")
            print(self.Status)
            time.sleep(1)
        dist.join()
        check.join()
    # Start 
    def threadControlRead(self, Houston, Status):
        sleepTime = 1
        while True:
            Houston.info("Control Panel Read.")
            Status = not Status
            time.sleep(sleepTime)
    def threadControlFix(self):
        sleepTime = 3
        while True:
            #Houston.info("Controls Fixed.")
            time.sleep(sleepTime)
    def threadSensorRead(self, Houston, Distance):
        sleepTime = 2
        while True:
            Houston.info("Sensors Read.")
            Distance = self.Voyager1.measureDistCM()
            time.sleep(sleepTime)
    def threadUpdateWorkout(self):
        sleepTime = 3
        while True:
            #Houston.info("Workout Updated.")
            time.sleep(sleepTime)
    def threadWriteStatus(self):
        sleepTime = 3
        while True:
            #Houston.info("Writing to Status File.")
            time.sleep(sleepTime)
    def threadSelfCheck(self):
        sleepTime = 3
        while True:
            #Houston.info("Running Self Check.")
            time.sleep(sleepTime)
"""Python Main Call"""
if __name__ == "__main__":
    # Create Controller Loop
    mainController = MainController()
    # Run Infinite Loop
    mainController.mainLoop()