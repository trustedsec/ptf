#!/usr/bin/env python
#####################################
# Installation module for Metagoofil
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Zawadi Done"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update Metagoofil"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/laramies/metagoofil"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="metagoofil"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,metagoofil"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION}"
