#!/usr/bin/env python
#####################################
# Installation module for hcxdumptool
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Corey Batiuk (skapunker)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update hcxdumptool - a tool for capturing wireless packets"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/ZerBea/hcxdumptool.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="hcxdumptool"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,build-essential,libcurl4-openssl-dev,libssl-dev,pkg-config"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,make,gcc"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},make,make install"

LAUNCHER="hcxdumptool"

BYPASS_UPDATES="YES"
