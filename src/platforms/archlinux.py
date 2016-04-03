#!/usr/bin/env python
#########################################
# Core installation for Archlinux Packages
#########################################
from src.core import logging
import subprocess

# this will do updates and installations


def base_install_modules(module_name):

    # will work for 1 or more space- or comma-separated modules
    modules = module_name.replace(",", " ")
    command = "pacman -S --needed --noconfirm " + modules
    subprocess.Popen(command, shell=True).wait()
