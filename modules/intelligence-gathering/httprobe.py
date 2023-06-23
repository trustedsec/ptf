#!/usr/bin/env python
####################################
# Installation module for httprobe #
####################################

# AUTHOR OF MODULE NAME
AUTHOR="Igibek Koishybayev"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update httprobe"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/tomnomnom/httprobe"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="httprobe"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,golang"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},go get,go build"

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER="httprobe"
