#!/usr/bin/env python
######################################
# Installation module for wifiphisher
######################################

# AUTHOR OF MODULE NAME
AUTHOR="Rémi HUGEUET (@shadawck)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update wifiphisher - A rogue Access Point framework."

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/wifiphisher/wifiphisher" 

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="wifiphisher"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git python3 dnsmasq libnl-3-dev libnl-genl-3-dev "

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},python3 setup.py install,cp {INSTALL_LOCATION}bin/wifiphisher /usr/bin/wifiphisher"

LAUNCHER=""
