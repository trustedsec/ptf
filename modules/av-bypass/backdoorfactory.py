#!/usr/bin/env python
#####################################
# Installation module for pyobfuscate
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Justin Herman (JDogHerman)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update BackDoor Factor (BDF) - AV Bypass"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/secretsquirrel/the-backdoor-factory"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="backdoor-factory"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN=""

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},chmod +x install.sh,./install.sh"
