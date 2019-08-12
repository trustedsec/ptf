#!/usr/bin/env python
#####################################
# Installation module for PCredz
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Andrew Schwartz"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update PCredz a tool that extracts Credit card numbers from a PCAP file or from a live ipnterface."

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/lgandx/PCredz"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="pcredz"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,python-libpcap"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,python-libpcap"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS=""

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER="pcredz"

# PREREQ INSTALL MODULES NEEDED FOR THIS TOOL TO WORK PROPERLY
TOOL_DEPEND=""
