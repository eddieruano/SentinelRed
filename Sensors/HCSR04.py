# -*- coding: utf-8 -*-
# @Author: eddieruano
# @Date:   2017-06-13 12:37:52
# @Last Modified by:   Eddie Ruano
# @Last Modified time: 2017-06-13 17:15:50
"""
    DESI uses two HCSR04 proximity sensors to determine Megan's postition on the treadmill.
"""
# Libraries
import RPi.GPIO as GPIO
import logging
import time

""" Initialization of Central Logger """
# Top Vars
LogLevel = logging.DEBUG        ## Change this later
LogLocation = "VoyagerLog.txt"
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

class HCSR04(object):
    def __init__(self, name, trigger, echo):
        self.Name = name
        self.TriggerPin = trigger
        self.EchoPin = echo
        self.Status = "Pass"
        
    def measureDistCM(self):
        StartTime = 0.0
        StopTime = 0.0
        TimeElapsed = 0.0
        # Warnings False to avoid Clutter to control module
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(trigger, GPIO.OUT)
        GPIO.setup(echo, GPIO.IN)
        # Set Trigger to HIGH
        GPIO.output(self.TriggerPin, True)
        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(self.triggerPin, False)
        # Create holders for times
        StartTime = time.time()
        # save StartTime
        TimeElapsed = StartTime
        while GPIO.input(self.EchoPin) == 0:
            StartTime = time.time()
            # if it goes too long
            if StartTime > (TimeElapsed + 0.1):
                Houston.error("Sensor " + self.Name + " took too long.")
                return(-1.0)
        # save time of arrival
        while GPIO.input(self.EchoPin) == 1:
        StopTime = time.time()
        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2
        # Release Pins
        GPIO.cleanup()
        return distance
        