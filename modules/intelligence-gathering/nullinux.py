#!/usr/bin/env python
#####################################
# Installation module for Nullinux
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Nick Dyer"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update Nullinux, a tool for enumerating SMB null sessions"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/m8r0wn/nullinux.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="nullinux"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="python,smbclient"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="python,smbclient"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},sh ./setup.sh"

# CREATE LAUNCHER
LAUNCHER="nullinux"
