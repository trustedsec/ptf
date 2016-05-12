#!/usr/bin/env python
#####################################
# Installation module for Maskprocessor
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Martin Bos (@purehate_)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update maskprocessor - High-Performance word generator with a per-position configureable charset"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/hashcat/maskprocessor.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="maskprocessor"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION}src/, make,cp mp64.bin ../maskprocessor"


# DONT RUN AFTER COMMANDS ON UPDATE
BYPASS_UPDATE=NO

# LAUNCHER
LAUNCHER="maskprocessor"

