#!/usr/bin/env python
#####################################
# Installation module for linuxprivchecker 
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="spinfoo"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update linuxprivchecker - Linux Privilege Escalation Check Script" 

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/sleventyeleven/linuxprivchecker.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="linuxprivchecker"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git python"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,python"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS=""

# create launcher
LAUNCHER="linuxprivchecker"
