#!/usr/bin/env python
######################################
# Installation module for unicornscan
######################################

# AUTHOR OF MODULE NAME
AUTHOR="Manuel Gines (xkulio)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update unicornscan (Network Scanner)"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/dneufeld/unicornscan.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="unicornscan"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,postgresql,libdnet-dev,libpq-dev,libpcap-dev,bison,flex"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git" # ToDo

# BYPASS UPDATES
BYPASS_UPDATE="YES"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},sed -i 's/inline//g' src/unilib/tsc.c,./configure CFLAGS=-D_GNU_SOURCE,make -j4,make install"


