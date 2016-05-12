#!/usr/bin/python
##########################
# After commands module
##########################
import subprocess
import os
from src.core import *

# this will execute after everything is over


def after_commands(command, install_location):
    # if there is more than one command iterate through
    if "," in command:
        # get current working directory
        definepath = os.getcwd()
        original_command = command
        command = command.split(",")

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
