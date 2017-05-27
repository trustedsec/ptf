#!/usr/bin/env python
#####################################
# Installation module for Old Interface Names
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="BustedSec (Frank_Trezza)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will force an ubuntu or debian machine to use the old naming convention for network interfaces such as eth0 or wlan0 instead of the new convention introduced into udev in recent kernal versions (tested on ubuntu 15.10, 16.04, and debian 8.6.0"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="FILE"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION=""

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION=""

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN=""

# DEPENDS FOR FEDORA INSTALLS
FEDORA=""

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="perl src/confset.pl GRUB_CMDLINE_LINUX=\""net.ifnames=0 biosdevname=0\"" /etc/default/grub, update-grub"



