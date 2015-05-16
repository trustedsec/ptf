#!/usr/bin/env python
#####################################
# Installation module for aircrack-ng
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Tim Fowler (roobixx)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update "

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/aircrack-ng/aircrack-ng"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="aircrack-ng"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="libsqlite3-devel"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS=""cd {INSTALL_LOCATION},make,make strip, make install,exit""
