#!/usr/bin/env python
#####################################
# Installation module for Wifite2
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Dave Kennedy (@HackingDave)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update wifite2 - a tool for wireless auditing"
# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/kimocoder/wifite2" 

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="wifite2"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git python3"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git python3"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},python3 setup.py install"

LAUNCHER=""

TOOL_DEPEND="modules/wireless/aircrackng"
