#!/usr/bin/env python
#####################################
# Installation module for Gobuster
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Liam Somerville (leesoh)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update OJ's Gobuster - a URL and DNS brute forcer"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/OJ/gobuster"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="gobuster"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,golang"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,golang"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="go get github.com/oj/gobuster,go get -u github.com/oj/gobuster"

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER=""

BYPASS_UPDATES="YES"
