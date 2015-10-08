#!/usr/bin/env python
#####################################
# Installation module for impacket
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Alberto Solino (@agsolino)" 

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update impacket, python exploitation framework"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/CoreSecurity/impacket"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="impacket"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION}, python setup.py install"
