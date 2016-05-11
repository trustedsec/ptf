#!/usr/bin/env python
#####################################
# Installation module for JohnTheRipper
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Martin Bos (@purehate_)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update John the Ripper. The "bleeding-jumbo" branch - An CPU-based password recovery tool.This is not "official" John the Ripper code"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/magnumripper/JohnTheRipper.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="johntheripper"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git libgmp3-dev git lzip gcc-multilib make m4 mingw-w64"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION}src,./configure,make"


# DONT RUN AFTER COMMANDS ON UPDATE
BYPASS_UPDATE=NO

# LAUNCHER
LAUNCHER="john"

