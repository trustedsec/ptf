#!/usr/bin/env python
#####################################
# Installation module for backdoo factory
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="David Kennedy (ReL1K)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update BackDoor Factor (BDF) - AV bypass"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/secretsquirrel/the-backdoor-factory"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="backdoor-factory"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,glibc-devel.i686,gcc"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},chmod +x install.sh,./install.sh"
LAUNCHER="backdoor"
