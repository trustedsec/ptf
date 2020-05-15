#!/usr/bin/env python
#####################################
# Installation module for HPing
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="AgentWhite (realagentwhite)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update HPing - Tool for checking status of hosts"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/realagentwhite/HPing"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="hping"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN=""

# DEPENDS FOR FEDORA INSTALLS
FEDORA=""

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="chmod 777 {INSTALL_LOCATION}"

# CREATE LAUNCHER
LAUNCHER="hping"
