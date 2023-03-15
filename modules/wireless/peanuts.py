#!/usr/bin/env python
#####################################
# Installation module for Peanuts
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Dave Kennedy (HackingDave)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update Peanuts, a free and open source wifi tracking tool."

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/sensepost/peanuts"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="peanuts"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git, python-pip, python-gps"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git"

LAUNCHER="peanuts"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},pip install -r requirements.txt"
