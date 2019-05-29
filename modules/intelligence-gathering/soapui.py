#!/usr/bin/env python
#######################################
# Installation module for Soap-UI
#######################################

# AUTHOR OF MODULE NAME
AUTHOR="Manuel Gines (xkulio)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install Soap-UI (API Testing)"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE, WGET
INSTALL_TYPE="WGET"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://s3.amazonaws.com/downloads.eviware/soapuios/5.5.0/SoapUI-x32-5.5.0.sh"

#X64 LOCATION
X64_LOCATION="https://s3.amazonaws.com/downloads.eviware/soapuios/5.5.0/SoapUI-x64-5.5.0.sh"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="soapui"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN=""

# DEPENDS FOR FEDORA INSTALLS
FEDORA="" # ToDo

# BYPASS UPDATES
BYPASS_UPDATE="YES"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},sh ./SoapUI-x64-5.5.0.sh"
