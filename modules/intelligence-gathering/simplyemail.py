#!/usr/bin/env python
#######################################
# Installation module for SimplyEmail
#######################################

# AUTHOR OF MODULE NAME
AUTHOR="David Kennedy (HackingDave)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update SimplyEmail - harvester tool for emails"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/killswitch-GUI/SimplyEmail"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="simplyemail"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION}/setup/,sh Setup.sh"

# CREATE LAUNCHER
LAUNCHER="SimplyEmail"
