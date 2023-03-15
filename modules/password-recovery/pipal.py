#!/usr/bin/env python
#####################################
# Installation module for pipal
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Larry Spohn (Spoonman)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/upgrade pipal - a tool for analyzing cracked password patterns and statistics"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/digininja/pipal.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="pipal"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="gem install levenshtein-ffi"

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER="pipal"
