#!/usr/bin/env python
#########################################
# Core installation for Debian Packages
#########################################
from src.core import logging
import subprocess

# this will do updates and installations
def base_install_modules(module_name):

    # if there is a , theres multiple modules
    if "," in module_name:
        module_name = module_name.split(",")
        # this will combine everything
        combined_modules = ""
        # iterate through tuple
        for modules in module_name:
            combined_modules = combined_modules + " " + modules

        subprocess.Popen("apt-get --force-yes -y install %s" % (combined_modules), shell=True).wait()

    else:
        # if its just one module
        if len(module_name) > 1:
            subprocess.Popen("apt-get --force-yes -y install " + module_name, shell=True).wait()
