#!/usr/bin/env python
#####################################
# Installation module for iodine
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="BustedSec (Frank Trezza)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update iodine - a tool for tunneling  IPv4 data through a DNS server. This can be usable in different situations where internet access is firewalled, but DNS queries are allowed. Reading http://dev.kryo.se/iodine/wiki/HowtoSetup is suggested"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/yarrick/iodine"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="iodine"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,make"

# DEPENDS FOR FEDORA INSTALLS
FEDORA=""

# CREATE LAUNCHER
LAUNCHER="iodine, iodined"
# FIX IODINED launcher later - framework not creating second launcher. 

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION}, make, ln -s {INSTALL_LOCATION}bin/iodine {INSTALL_LOCATION}iodine, ln -s {INSTALL_LOCATION}bin/iodined {INSTALL_LOCATION}iodined" 




