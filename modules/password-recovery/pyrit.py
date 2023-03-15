#!/usr/bin/env python
#####################################
# Installation module for Pyrit
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Dave Kennedy (ReL1K)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update pyrit - fast password generation db for wireless"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE ,wget
INSTALL_TYPE="git"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/JPaulMora/Pyrit"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="pyrit"

#not github program manual update of the link needed
BYPASS_UPDATE="NO"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},python setup.py install"

LAUNCHER="pyrit"
