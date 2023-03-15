#!/usr/bin/env python
#####################################
# Installation module for lsassy
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Andrew Schwartz"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update lsassy by HackAndDo (@HackAndDo) - A tool to remotely parse lsass dumps and extract credentials."

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/Hackndo/lsassy.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="lsassy"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="python3.7,pypkatz,impacket"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},python3.7 setup.py install"

LAUNCHER="lsassy"

# PREREQ INSTALL MODULES NEEDED FOR THIS TOOL TO WORK PROPERLY
TOOL_DEPEND="modules/exploitation/impacket"

TOOL_DEPEND="modules/post-exploitation/pypykatz"
