#!/usr/bin/env python
#####################################
# Installation module for InSpy
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Jason Ashton (ninewires)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update InSpy - A LinkedIn enumeration tool"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/gojhonny/InSpy"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="InSpy"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,python-pip"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git"

# DEPENDS FOR ARCHLINUX INSTALLS
ARCHLINUX=""

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION}, pip install -r requirements.txt"

# create a launcher
LAUNCHER="InSpy"
