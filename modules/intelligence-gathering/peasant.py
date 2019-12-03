#!/usr/bin/env python
#######################################
# Installation module for Peasant
#######################################

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update Peasant by Justin Angel (@arch4ngel) - A LinkedIn reconnaissance utility written in Python3 that functions much like LinkedInt by @vysecurity."

AUTHOR="Andrew Schwartz"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/arch4ngel/peasant.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="peasant"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,pip,python3"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},python3 -m pip install -r requirements.txt"

LAUNCHER="peasant"
