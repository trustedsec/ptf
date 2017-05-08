#!/usr/bin/env python
#####################################
# Installation module to install dradis as a service
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="BustedSec (Frank_Trezza)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install conky with a custom config written by gotm1lk originally designed for kali, requires ptf modules/user-submitted/old-interface-names be installed"
# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="git"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/BustedSec/conky-customconfig.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="conky-customconfig"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN=""

# DEPENDS FOR FEDORA INSTALLS
FEDORA=""

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION}, chmod +x conkyinstall.sh, ./conkyinstall.sh"


