# -*- coding: utf-8 -*-
# @Author: Eddie Ruano
# @Date:   2017-06-13 11:11:04
# @Last Modified by:   Eddie Ruano
# @Last Modified time: 2017-06-16 13:09:35
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
import Sensors.MPR121 as MPR121

# Localities
#from .Sensors import HCSR04

""" Initialization of Central Logger """
# Top Vars
LogLevel = logging.DEBUG        ## Change this later
LogLocation = "Logs/MainLog.txt"
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

"""#### BEGIN MAIN CONTROLLER CLASS ####"""

class MainController(object):
    global Houston # Need to access the Logger
    Distance = 0.0
    Status = True
    Voyager1 = HCSR04.HCSR04("Voyager1", 17, 4)
    TouchSensor = MPR121.MPR121()
    def __init__(self):
        pass
    def mainLoop(self):
        # Create the threads
        try:  
            # here you put your main loop or block of code  
            # Start the threads
            while True:
                
                time.sleep(5)
        except KeyboardInterrupt:  
            # Code runs before the program exits w/ CTRL+C
            Houston.info("Mission Shutdown By Supervisor")
        except:  
            # this catches ALL other exceptions including errors.  
            # You won't get any error messages for debugging  
            # so only use it once your code is working  
            Houston.error("Error occurred. Caught in Last Except")
        finally:  
            # this ensures a clean exit with GPIO PINS
            GPIO.cleanup() 
            Houston.info("Finally Mission was Shutdown.")
    ##### END OF MAIN CONTROLLER FUNCTION #####
    # THREADS
    def threadControlRead(self, Houston, Status):
        sleepTime = 1
        Houston.info("Control Panel Read.")
        Status = False
        time.sleep(sleepTime)
    def makeLogs(self):
        pass
        #import os, os.path
        #if not os.path.exists("qe/logs/"):
        #os.makedirs("qe/logs/")

"""Python Main Call"""
if __name__ == "__main__":
    # Create Controller Loop
    mainController = MainController()
    # Run Infinite Loop
    mainController.mainLoop()
    #     def threadControlFix(self):
    #     sleepTime = 3
    #     while True:
    #         #Houston.info("Controls Fixed.")
    #         time.sleep(sleepTime)
    # def threadSensorRead(self, Houston):
    #     global Distance
    #     sleepTime = 2
    #     Houston.info("Sensors Read.")
    #     Distance = self.Voyager1.measureDistCM()
    # def threadUpdateWorkout(self):
    #     sleepTime = 3
    #     while True:
    #         #Houston.info("Workout Updated.")
    #         time.sleep(sleepTime)
    # def threadWriteStatus(self):
    #     sleepTime = 3
    #     while True:
    #         #Houston.info("Writing to Status File.")
    #         time.sleep(sleepTime)
    # def threadSelfCheck(self):
    #     sleepTime = 3
    #     while True:
    #         #Houston.info("Running Self Check.")
    #         time.sleep(sleepTime)