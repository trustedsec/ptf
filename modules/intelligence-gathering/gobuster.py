#!/usr/bin/env python
####################################
# Installation module for Gobuster #
####################################

# AUTHOR OF MODULE NAME
AUTHOR="Zawadi Done"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update GoBuster"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/OJ/gobuster"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="gobuster"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,golang"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},go get,go build"

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER="gobuster"
