# -*- coding: utf-8 -*-
# @Author: Eddie Ruano
# @Date:   2017-06-14 08:40:00
# @Last Modified by:   Eddie Ruano
# @Last Modified time: 2017-06-14 09:35:16
import threading
import time
import random

class threadQueryDistance(threading.Thread):

	def __init__(self, name):
		threading.Thread.__init__(self)
		self.name = name
	