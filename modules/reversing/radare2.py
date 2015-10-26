#!/usr/bin/env python
#####################################
# Installation module for radare2
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Mauro Risonho de Paula Assumpção (firebits)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update radare2 - is a portable reversing framework"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/radare/radare2"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="radare2"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,make,gcc"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,make,gcc"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},sys/install.sh"

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER="radare2"

