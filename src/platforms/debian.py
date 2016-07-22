#!/usr/bin/env python
#
# Core installation for Debian Packages
#
from src.core import logging
import subprocess

# this will do updates and installations


def base_install_modules(module_name):

    counter = 0
    # will work for 1 or more space- or comma-separated modules
    modules = module_name
    if "," in modules:
        modules = modules.split(",")
        counter = 1
    if " " in modules:
        modules = modules.split(",")
        counter = 1

    # just in case spaces
    # this might take a little longer but its worth it incase there are depend
    # issues with versions and they don't install it doesn't bork the rest of
    # depends
    if counter == 1:
        for module in modules:
            command = ("apt-get -q --force-yes -y install " + module)
            subprocess.Popen("export DBEIAN_FRONTEND=noninteractive;%s" %
                             command, shell=True).wait()
    else:
        command = ("apt-get -q --force-yes -y install " + modules)
        subprocess.Popen("export DEBIAN_FRONTEND=noninteractive;%s" %
                         command, shell=True).wait()
