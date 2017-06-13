# -*- coding: utf-8 -*-
# @Author: eddieruano
# @Date:   2017-06-13 14:09:55
# @Last Modified by:   eddieruano
# @Last Modified time: 2017-06-13 14:54:37
import time
from .Sensors import HCSR04
from .Sensors import MPR121

class SensorManager(object):
    def __init__(self, name, t1, e1, t2, e2):
        self.Name = name
        self.Touch = MPR121()
        self.Voyager1 = HCSR04(t1, e1)
        self.Voyager2 = HCSR04(t2, e2)
        self.updateThisIteration = False
        time.sleep(0.1)
        self._cachedData = {}
        self.currentV1Dist = None
        self.currentV2Dist = None
        self.currentTouchVal = 0
    def _clearCache(self):
        self._cachedData = {}
    def tick(self):
        self._clearCache()
        self.updateThisIteration = False
    def getSensorPayload()