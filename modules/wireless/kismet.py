#!/usr/bin/env python
#####################################
# Installation module for kismet
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Dave Kennedy (HackingDave)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update kismet, a tool for wireless auditing"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/kismetwireless/kismet"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="kismet"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,libnl-3-dev,libnl-cli-3-dev,libmicrohttpd-dev,libprotobuf-dev,protobuf-compiler,libprotobuf-c-dev,libprotoc-dev,protobuf-c-compiler"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},./configure, make,make install"
