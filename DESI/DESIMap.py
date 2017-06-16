# -*- coding: utf-8 -*-
# @Author: Eddie Ruano
# @Date:   2017-06-16 03:47:18
# @Last Modified by:   Eddie Ruano
# @Last Modified time: 2017-06-16 04:16:52
import RPi.GPIO as GPIO
import time

class DESI(object):

    """Representation of a DESI Entity"""
    # Control Box Pins
    IN_START    = 9
    IN_PAUSE    = 10
    IN_SPEED0   = 11
    IN_SPEED1   = 5
    IN_SPEED2   = 6
    IN_SPEED3   = 13
    IN_SPEED4   = 19
    # Proximity Sensor Pins
    PROX1_TRIG  = 17
    PROX1_ECHO  = 4
    PROX2_TRIG  = 22
    PROX2_ECHO  = 27
    # Relay Pins
    OUT_START   = 14
    OUT_OFF     = 15
    OUT_PAUSE   = 18
    OUT_ENTER   = 23
    OUT_0       = 24
    OUT_1       = 25
    OUT_2       = 8
    OUT_3       = 7
    OUT_4       = 21
    OUT_5       = 16
    OUT_DOWN    = 12
    """ Initialization of DESIMAP Logger """
    # Top Vars
    LogLevel = logging.DEBUG        ## Change this later
    LogLocation = "Logs/DESIMAPLog.txt"
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
    def __init__(self):
        """Start the pin mapping operation."""
        self._initDESI() # This sets modeGPIO, no warn + control pins + relays
    def _initDESI(self):
        # Set up GPIO stuff
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False) #check
        self.initControlBox()
        self.initRelays()
    def _initControlBox(self):
        GPIO.setup(self.IN_START, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.IN_PAUSE, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.IN_SPEED0, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.IN_SPEED1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.IN_SPEED2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.IN_SPEED3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.IN_SPEED4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        print ("Buttons Complete.")
    def _initRelays(self):
        # Set up the correct In/Out Scheme for send/receive
        GPIO.setup(self.OUT_START, GPIO.OUT)
        GPIO.setup(self.OUT_OFF, GPIO.OUT)
        GPIO.setup(self.OUT_PAUSE, GPIO.OUT)
        GPIO.setup(self.OUT_ENTER, GPIO.OUT)
        GPIO.setup(self.OUT_0, GPIO.OUT)
        GPIO.setup(self.OUT_1, GPIO.OUT)
        GPIO.setup(self.OUT_2, GPIO.OUT)
        GPIO.setup(self.OUT_3, GPIO.OUT)
        GPIO.setup(self.OUT_4, GPIO.OUT)
        GPIO.setup(self.OUT_5, GPIO.OUT)
        GPIO.setup(self.OUT_DOWN, GPIO.OUT)
        #GPIO.setup(self.OUT_ALEXA, GPIO.OUT)
        GPIO.output(self.OUT_START, GPIO.HIGH)
        GPIO.output(self.OUT_OFF, GPIO.HIGH)
        GPIO.output(self.OUT_PAUSE, GPIO.HIGH)
        GPIO.output(self.OUT_ENTER, GPIO.HIGH)
        GPIO.output(self.OUT_0, GPIO.HIGH)
        GPIO.output(self.OUT_1, GPIO.HIGH)
        GPIO.output(self.OUT_2, GPIO.HIGH)
        GPIO.output(self.OUT_3, GPIO.HIGH)
        GPIO.output(self.OUT_4, GPIO.HIGH)
        GPIO.output(self.OUT_5, GPIO.HIGH)
        GPIO.output(self.OUT_DOWN, GPIO.HIGH)
        #GPIO.output(self.OUT_ALEXA, GPIO.HIGH)
        print ("Relay Array Set.")