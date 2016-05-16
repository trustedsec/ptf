#!/usr/bin/env python
#####################################
# Installation module for DNSEnum
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Brice Samulenok (BriceTheGrey)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update dirb - A URL Bruteforcer"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/seifreed/dirb.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="dirb"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git"

# COMMANDS TO RUN AFTER 
AFTER_COMMANDS="cd {INSTALL_LOCATION},./configure,make"

# create a launcher
LAUNCHER="dirb"
