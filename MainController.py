# -*- coding: utf-8 -*-
# @Author: Eddie Ruano
# @Date:   2017-06-13 11:11:04
# @Last Modified by:   eddieruano
# @Last Modified time: 2017-06-13 15:03:20
"""
    MainController contains all threading control logic
"""
import time
import datetime
import os
import gevent
from gevent import monkey
import logging

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
    def __init__(self):
        pass
    # Start 
    def threadControlRead(self):
        sleepTime = 3
        while True:
            Houston.info("Control Panel Read.")
            time.sleep(sleepTime)
    def threadControlFix(self):
        sleepTime = 3
        while True:
            Houston.info("Controls Fixed.")
            time.sleep(sleepTime)
    def threadSensorRead(self):
        sleepTime = 3
        while True:
            Houston.info("Sensors Read.")
            time.sleep(sleepTime)
    def threadUpdateWorkout(self):
        sleepTime = 3
        while True:
            Houston.info("Workout Updated.")
            time.sleep(sleepTime)
    def threadWriteStatus(self):
        sleepTime = 3
        while True:
            Houston.info("Writing to Status File.")
            time.sleep(sleepTime)
    def threadSelfCheck(self):
        sleepTime = 3
        while True:
            Houston.info("Running Self Check.")
            time.sleep(sleepTime)
    def mainLoop(self):
        greenLets = []
        greenLets.append(gevent.spawn(self.threadControlRead))
        greenLets.append(gevent.spawn(self.threadControlFix))
        greenLets.append(gevent.spawn(self.threadSensorRead))
        gevent.joinall(all_greenlets)
"""Python Main Call"""
if __name__ == "__main__":
    monkey.patch_all()
    mainController = MainController()
    mainController.mainLoop()