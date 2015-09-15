#!/usr/bin/env python
#####################################
# Installation module for splint
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Mauro Risonho de Paula Assumpcao (firebits)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update splint, a tool for static C/C++ Code"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="wget http://www.splint.org/downloads/splint-3.1.2.src.tgz" 

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="splint-3.1.2"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="gcc,make,gzip,tar,automake"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="tar xzf splint-3.1.2.src.tgz,cd {INSTALL_LOCATION},configure,make,make install"
