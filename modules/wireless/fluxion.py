#!/usr/bin/env python
#####################################
# Installation module for Wifite
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Frank Trezza (thatrez)"

# DESCRIPTION OF THE MODUL
DESCRIPTION="This module will install/update fluxion - a fake access point designed to trick users into divulgining wifi passwords"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/deltaxflux/fluxion" 

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="fluxion"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="bully"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},bash Installer.sh"

LAUNCHER="fluxion"
