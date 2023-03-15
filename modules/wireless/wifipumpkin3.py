#!/usr/bin/env python
#####################################
# Installation module for Wifipumpkin3
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Dave Kennedy (@HackingDave)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update wifipumpkin3 - a tool for rogue access points"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/P0cL4bs/wifipumpkin3" 

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="wifipumpkin3"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git python3.7-dev libssl-dev libffi-dev build-essential python3"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git python3.7"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},make install"

LAUNCHER=""
