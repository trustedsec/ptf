#!/usr/bin/python
##########################
# After commands module
##########################
#import pexpect
import subprocess
import os
from src.core import *

# this will execute after everything is over
def after_commands(command):
    # if there is more than one command iterate through
    if "," in command:
	# get current working directory
	definepath = os.getcwd()
	original_command = command
        command = command.split(",")
	
	# we have to do some funky stuff for metasploit - main issue is that since we source rvm.sh - subprocess isn't technically using bash, so the source paths don't work - what we'll do is write out a file instead and run it via bash.
	if "get.rvm.io" in original_command:
		print_status("Metasploit install detected, doing some funky magic...")
		filewrite = file("meta_temp.sh", "w")
		filewrite.write("#!/bin/bash\n")
		for commands in command:
			if "/metasploit" in commands:
				install_location = commands
			filewrite.write(commands + " && ")
		filewrite.write("echo")
		filewrite.close()
		print_status("Running shell to install Metasploit and source rvm.sh")
		subprocess.Popen("chmod +x meta_temp.sh", shell=True).wait()
		subprocess.Popen("./meta_temp.sh", shell=True).wait()
		if os.path.isfile("meta_temp.sh"): os.remove("meta_temp.sh")
		#filewrite = file("meta_temp.sh", "w")
		#filewrite.write("#!/bin/bash\nsource /etc/profile.d/rvm.sh\n%s\ngem install bundler\nbundle install" % (install_location))
		#filewrite.close()
		#print_status("Running bundler again..")
		#subprocess.Popen("chmod +x meta_temp.sh;./meta_temp.sh", shell=True).wait()
		print_status("I think we're finished here... Moving on.")

	else:
		# iterate through commands
	        for commands in command:
			print_status("Sending after command: " + commands)
			# change directory if CD in command
			if "cd " in commands:
				commands = commands.replace("cd ", "")
				if os.path.isdir(commands):
					os.chdir(commands)
			else:
				subprocess.Popen(commands, shell=True).wait()

		# restore original directory
		os.chdir(definepath)

    else:
	subprocess.Popen(command, shell=True).wait()

