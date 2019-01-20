#!/usr/bin/env python
#####################################
# Installation module for SMBMap
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Corey Batiuk (Skapunker)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update the SMB enumeration tool SMBMap"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/ShawnDEvans/smbmap"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="smbmap"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,python-pip"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,python-pip"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},pip install -r requirements.txt"

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER="smbmap"

# PREREQ INSTALL MODULES NEEDED FOR THIS TOOL TO WORK PROPERLY
TOOL_DEPEND=""
