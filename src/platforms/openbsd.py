#!/usr/bin/env python
########################################
# Core installation for OpenBSD Packages
########################################
from src.core import logging
import subprocess

# this will do updates and installations


def base_install_modules(module_name):

    # will work for 1 or more space- or comma-separated modules
    modules = module_name.replace(",", " ")
    command = "pkg_add -Uu && pkg_add -ui && pkg_add -uvi " + modules
    subprocess.Popen(command, shell=True).wait()
