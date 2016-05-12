#!/usr/bin/env python
#####################################
# Installation module for cfr
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Jens Muecke (ryd)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update rats, a tool for static C/C++ Code"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="SVN"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="http://rough-auditing-tool-for-security.googlecode.com/svn/trunk/" 

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="rats"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="build-essential,cmake,subversion"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="subversion,make,cmake,automake,gcc,gcc-c++,kernel-devel,expat-devel"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},./configure,make,make install"

LAUNCHER="rats"
