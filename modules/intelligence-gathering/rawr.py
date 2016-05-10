#!/usr/bin/env python
#######################################
# Installation module for RAWR
#######################################

# AUTHOR OF MODULE NAME
AUTHOR="Justin Herman (JDogHerman)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update RAWR - Rapid Assessment of Web Resources."

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://bitbucket.org/al14s/rawr.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="rawr"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,libffi-dev"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},./install.sh y"
