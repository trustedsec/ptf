#!/usr/bin/env python
#####################################
# Installation module for urlcrazy
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Dave Kennedy and jayw0k"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update urlcrazy (needed for discover)."

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="FILE"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="http://www.morningstarsecurity.com/downloads/urlcrazy-0.5.tar.gz"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="urlcrazy"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN=""

# DEPENDS FOR FEDORA INSTALLS
FEDORA=""

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},make,make install"

LAUNCHER="urlcrazy"
