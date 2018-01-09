#!/usr/bin/env python
#####################################
# Installation module for gpp-decrypt
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Larry Spohn (Spoonman)"
AUTHOR="Frank Trezza (bustedsec)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/upgrade gpp-decrypt - a tool for decrypting passwords found in Group Policy Preferences (GPP)"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/BustedSec/gpp-decrypt"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="gpp-decrypt"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git"

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER="gpp-decrypt"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd /usr/local/bin, sed -i 's/.\/gpp-decrypt.rb/ruby gpp-decrypt.rb/g' gpp-decrypt"


