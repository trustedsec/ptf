#!/usr/bin/env python
#####################################
# Installation module for masscan
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Mauro Risonho de Paula Assumpcao (firebits)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update masscan - a quick TCP/SYN port scanner"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/robertdavidgraham/masscan.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="masscan"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,gcc,make,libpcap-dev"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,gcc,make,libpcap-devel"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},make -j,cp bin/masscan ."

LAUNCHER="masscan"

