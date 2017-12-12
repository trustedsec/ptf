#!/usr/bin/env python
#####################################
# Installation module for RPIVOT
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="BustedSec (Frank Trezza)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update hans. Hans allows you to tunnel IPv4 through ICMP echo packets, so you could call it a ping tunnel. This can be useful when you find yourself in the situation that your Internet access is firewalled, but pings are allowed."

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/friedrich/hans.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="hans"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,make"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,make"

# CREATE LAUNCHER
LAUNCHER="hans"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},make"
