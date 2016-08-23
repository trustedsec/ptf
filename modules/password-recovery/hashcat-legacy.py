#!/usr/bin/env python
#####################################
# Installation module for Hashcat (Legacy)
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Martin Bos (@purehate_)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install Hashcat (Legacy Version)- An advanced CPU-based password recovery"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/hashcat/hashcat-legacy.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="hashcat-legacy"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="ocl-icd-opencl-dev libgmp3-dev git lzip gcc-multilib make m4 mingw-w64 libgmp3-dev:i386"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},make linux"

# DONT RUN AFTER COMMANDS ON UPDATE
BYPASS_UPDATE=NO

# LAUNCHER
LAUNCHER="hashcat"
