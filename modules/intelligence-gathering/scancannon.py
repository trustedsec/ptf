#!/usr/bin/env python
#####################################
# Installation module for ScanCannon
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Dave Kennedy (ReL1K)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update ScanCannon - features of masscan and nmap combined (need to install masscan module first)"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/johnnyxmas/ScanCannon"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="scancannon"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,nmap"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,nmap"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS=""

LAUNCHER="scancannon"

