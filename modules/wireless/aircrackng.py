#!/usr/bin/env python
#####################################
# Installation module for aircrack-ng
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Tim Fowler (roobixx)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update aircrack-ng, a tool for wireless attacks"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/aircrack-ng/aircrack-ng" 

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="aircrack-ng"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="libsqlite3-dev,libnl-3-dev,libnl-cli-3-dev,pkg-config,libtool"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,libsqlite3x-devel,libnl3-devel,libnl-genl-3-dev,libtool"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},./autogen.sh,make -j4,make strip,sed -i 's|http://standards-oui.ieee.org/oui.txt|http://linuxnet.ca/ieee/oui.txt|g' scripts/airodump-ng-oui-update,make install,airodump-ng-oui-update"
