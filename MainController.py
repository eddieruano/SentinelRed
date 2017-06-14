# -*- coding: utf-8 -*-
# @Author: Eddie Ruano
# @Date:   2017-06-13 11:11:04
# @Last Modified by:   Eddie Ruano
# @Last Modified time: 2017-06-13 17:47:18
"""
    MainController contains all threading control logic
"""
import RPi.GPIO as GPIO
import logging
import os
import sys
import threading
import time
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


class MainController(object):
    global Houston
    Distance = 0.0
    Status = True
    Voyager1 = HCSR04.HCSR04("Voyager1", 17, 4)
    def __init__(self):
        pass
    def mainLoop(self):
        # Create the threads
        dist = threading.Thread(name='ThreadV1', target=self.threadSensorRead, args=(Houston, self.Distance))
        check = threading.Thread(name='CheckC', target=self.threadControlRead, args=(Houston, self.Status))
        dist.setDaemon(True)
        check.setDaemon(True)
        try:
            # Start the threads
            dist.start()
            check.start()

            while True:
                Houston.info("In the loop")
                Houston.info("Dist: ")
                Houston.info(self.Distance)
                Houston.info("Status: ")
                Houston.info(self.Status)
                time.sleep(5)
        except KeyboardInterrupt:
            GPIO.cleanup()
            dist.join()
            check.join()
            print("Shutdown Mission.")
    # THREADS
    def threadControlRead(self, Houston, Status):
        sleepTime = 1
        Houston.info("Control Panel Read.")
        Status = False
        time.sleep(sleepTime)
    def threadControlFix(self):
        sleepTime = 3
        while True:
            #Houston.info("Controls Fixed.")
            time.sleep(sleepTime)
    def threadSensorRead(self, Houston, Distance):
        sleepTime = 2
        Houston.info("Sensors Read.")
        Distance = self.Voyager1.measureDistCM()
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