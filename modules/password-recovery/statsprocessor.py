#!/usr/bin/env python
#####################################
# Installation module for Statsprocessor
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Martin Bos (@purehate_)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update Statsprocessor - Statsprocessor is a word-generator based on per-position markov-chains packed into a single stand-alone binary"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/hashcat/statsprocessor.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="statsprocessor"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION}src/, make,cp sp64.bin ../statsprocessor"


# DONT RUN AFTER COMMANDS ON UPDATE
BYPASS_UPDATE=NO

# LAUNCHER
LAUNCHER="statsprocessor"

