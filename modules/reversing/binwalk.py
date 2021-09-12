#!/usr/bin/env python
#####################################
# Installation module for binwalk
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Jens Muecke (ryd)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update binwalk - a Firmware Analysis Tool"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/ReFirmLabs/binwalk"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="binwalk"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,python-lzma"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},python3 setup.py install --prefix=/usr/local"
