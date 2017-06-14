# -*- coding: utf-8 -*-
# @Author: Eddie Ruano
# @Date:   2017-06-13 11:11:04
# @Last Modified by:   Eddie Ruano
# @Last Modified time: 2017-06-13 17:14:48
"""
    MainController contains all threading control logic
"""
import logging
import threading
import time

from Sensors import HCSR04

# Localities
#from .Sensors import HCSRO4

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
HoustonLog.addHandler(HouStream)
HoustonLog.addHandler(HouFile)
Houston.info("Logger has been created.")
""" Initialization of Global Variables """

class MainController(object):
    global Houston
    Distance = 0.0
    Status = True
    Voyager1 = HCSRO4("Voyager1", 17, 4)
    def __init__(self):
        pass
    def mainLoop(self):
        # Create the threads
        dist = threading.Thread(name="ThreadV1", target=threadSensorRead, args=(Houston, self.Distance))
        check = threading.Thread(name="CheckC", target=threadControlRead, args=(Houston, self.Status))
        # Start the threads
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