#!/usr/bin/env python
#####################################
# Installation module for nmap-dev
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Mauro Risonho de Paula Assumpcao (firebits), updated by Russ Swift (0xsalt)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update Nmap (Network Mapper) and Ncat (Fyodor's Netcat)"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="SVN"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://svn.nmap.org/nmap/"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="nmap"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="subversion,autoconf,build-essential,libssl-dev"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="subversion,autoconf,make,automake,gcc,gcc-c++,kernel-devel,openssl-devel"

# BYPASS UPDATES
BYPASS_UPDATE="YES"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},./configure,make,make install,cd {INSTALL_LOCATION}/ncat,./configure,make,make install"
