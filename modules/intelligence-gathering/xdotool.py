#!/usr/bin/env python
#####################################
# Installation module for xdotool
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Jason Ashton (@jayw0k)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update xdotool - a keyboard/mouse activity simulator"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/jordansissel/xdotool.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="xdotool"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,make,libx11-dev,libxtst-dev"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="make,libx11-devel,libxtst-devel"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},make,make install"

# CREATE LAUNCHER
LAUNCHER="xdotool"
