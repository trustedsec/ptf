#!/usr/bin/env python
#####################################
# Installation module for dot11decrypt
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Joao Pena Gil (Jack64)"

# DESCRIPTION OF THE MODULE  
DESCRIPTION="This module will install/update dot11decrypt, a WEP/WPA2(AES and TKIP) on-the-fly decrypter."

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/mfontanini/dot11decrypt/"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="dot11decrypt"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN=""

# DEPENDS FOR FEDORA INSTALLS
FEDORA=""

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},./configure,make,make install"
