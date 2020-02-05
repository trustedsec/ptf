#!/usr/bin/env python
#####################################
# Installation module for Spiderfoot
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Paul White (@Su1ph3r)"

#DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update Spiderfoot"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/smicallef/spiderfoot.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="spiderfoot"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git python3-pip"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},pip3 install -r requirements.txt"

# create a launcher
LAUNCHER="spiderfoot"
