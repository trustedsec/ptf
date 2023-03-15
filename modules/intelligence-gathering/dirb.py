#!/usr/bin/env python
#####################################
# Installation module for Dirb
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Manuel Gines (xkulio)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update dirb - A URL Bruteforcer by Ramon Pinuaga"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/v0re/dirb.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="dirb"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,libcurl4,libcurl4-openssl-dev"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git" # ToDo

# BYPASS UPDATES
BYPASS_UPDATE="YES"

# COMMANDS TO RUN AFTER 
AFTER_COMMANDS="cd {INSTALL_LOCATION},./configure,make,make install,mkdir /usr/share/dirb,cp -R wordlists /usr/share/dirb"

