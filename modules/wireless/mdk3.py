#!/usr/bin/env python
#####################################
# Installation module for mdk3
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="jklaz"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update mdk3, a tool for wireless attacks"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/wi-fi-analyzer/mdk3-master" 

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="mdk3-master"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,libpcap-dev"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,libpcap-devel"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},make,make strip,make install"
