#!/usr/bin/env python
#####################################
# Installation module for Princeprocessor
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Martin Bos (@purehate_)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update Princeprocessor - Standalone password candidate generator using the PRINCE algorithm"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/hashcat/princeprocessor.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="princeprocessor"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN=""

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION}src/, make"


# DONT RUN AFTER COMMANDS ON UPDATE
BYPASS_UPDATE=NO

# LAUNCHER
LAUNCHER="princeprocessor"

