#!/usr/bin/env python
#####################################
# Installation module for cfr
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Jens Muecke (ryd)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update flawfinder, a tool for static C/C++ Code"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="http://git.code.sf.net/p/flawfinder/code" 

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="flawfinder"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="build-essential,git"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,make,automake,gcc,gcc-c++,kernel-devel"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},make install"

LAUNCHER="flawfinder"
