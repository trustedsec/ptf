#!/usr/bin/env python
#####################################
# Installation module for ipcrawl
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Ben Drysdale"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update ipcrawl by dmuz @ AngryPacket - enumerate DNS by IP address"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/BenDrysdale/ipcrawl/"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="ipcrawl"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,gcc"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,gcc"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},gcc ipcrawl.c -o ipcrawl,chmod +x ipcrawl"

# CREATE LAUNCHER
LAUNCHER="ipcrawl"
