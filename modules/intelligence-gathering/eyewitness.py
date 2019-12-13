#!/usr/bin/env python
#######################################
# Installation module for eyewitness
#######################################

# AUTHOR OF MODULE NAME
AUTHOR="Kirk Hayes (l0gan)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update EyeWitness."

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/FortyNorthSecurity/EyeWitness"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="eyewitness"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,python-setuptools,libffi-dev,libssl-dev"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION}/setup,./setup.sh"

LAUNCHER="eyewitness"
