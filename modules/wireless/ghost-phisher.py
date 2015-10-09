#!/usr/bin/env python
#####################################
# Installation module for ghost-phisher
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Mauro Risonho de Paula Assumpcao (firebits)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update ghost-phisher - emulate access points and deploy various internal networking servers for networking, penetration testing and phishing attacks."

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/savio-code/ghost-phisher.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="ghost-phisher"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,python2.7,python-qt4,isc-dhcp-server,ettercap-graphical"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,dhcp-server,ettercap,PyQt4,scapy"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS=""
