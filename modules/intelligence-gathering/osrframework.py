#!/usr/bin/env python
#####################################
# Installation module for testSSL
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Félix Brezo and Yaiza Rubio (@i3visio)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update Open Sources Research Framework (OSRFramework)."

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/i3visio/osrframework.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="osrframework"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git python-pip"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git"

# DEPENDS FOR ARCHLINUX INSTALLS
ARCHLINUX=""

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="pip install osrframework --upgrade"
