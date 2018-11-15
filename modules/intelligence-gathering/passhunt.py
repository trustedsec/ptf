#!/usr/bin/env python3
#####################################
# Installation module PASSHUNT
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Zawadi Done"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update Passhunt"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/Viralmaniar/Passhunt"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="passhunt"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,python3,python3-pip"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},pip3 install -r requirements.txt"

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER="passhunt"
