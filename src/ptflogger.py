#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
This script is only for logging the output of commands that are given to PTF through arguments 
and it's internal command line (ptf> )

This is still under development so do not expect it to work perfectly... yet.
'''

import logging
from src.core import print_error, bcolors
import sys
import os
'''
DEBUG
	Detailed information, typically of interest only when diagnosing problems.
INFO
	Confirmation that things are working as expected.
WARNING
	An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
ERROR
	Due to a more serious problem, the software has not been able to perform some function.
CRITICAL
	A serious error, indicating that the program itself may be unable to continue running.
'''


try:
	# Setting logging output configuration TESTING ONLY!!!
	''' *************************************************** '''

	# First check if the file exists, if it does emtpy the file with /dev/null

	if os.path.isfile("ptf-output.log"):
		os.system("cat /dev/null > ptf-output.log")

	log = logging.basicConfig(filename="ptf-output.log", level=logging.INFO)
	#log = logging.getLogger("PTF Basic Logger")
	log = logging.info

	info = logging.info
	debug = logging.debug
	error = logging.error
	critical = logging.critical
	''' *************************************************** '''
except Exception as error:
	print_error("Ooops! There seems to be a mistake somewhere in src.ptflogger module")
	print_error(error)
	sys.exit()
