#!/usr/bin/env python
#########################################
# Installation module for KrbRelayX
#########################################

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update KrbRelayX by Dirk-Jan (@_dirkjan) - A Toolkit for abusing Unconstrained Delegation."

AUTHOR="Andrew Schwartz"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/dirkjanm/krbrelayx.git"

#WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="krbrelayx"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,impacket,ldap3"

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER="krbrelayx"

TOOL_DEPEND="modules/exploitation/impacket"

# PREREQ INSTALL MODULES NEEDED FOR THIS TOOL TO WORK PROPERLY
TOOL_DEPEND=""
