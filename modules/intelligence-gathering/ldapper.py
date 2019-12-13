#!/usr/bin/env python
#####################################
# Installation module for LDAPPER
#####################################

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update ldapper a command line tool to query AD via LDAP"

AUTHOR="Andrew Schwartz"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/shellster/LDAPPER.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="ldapper"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,python3-ldap3, python3-yaml, python3-colorama"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,python3-ldap3, python3-yaml, python3-colorama"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},pip install -r requirements.txt"

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER="ldapper"

# PREREQ INSTALL MODULES NEEDED FOR THIS TOOL TO WORK PROPERLY
TOOL_DEPEND=""
