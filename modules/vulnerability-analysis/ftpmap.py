#!/usr/bin/env python
#####################################
# Installation module for ftpmap
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Hypsurus"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update ftpmap (ftp scanner)."

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/Hypsurus/ftpmap"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="ftpmap"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="autoconf,build-essential,libssl-dev"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,autoconf,make,automake,gcc,gcc-c++,kernel-devel,openssl-devel"

# DEPENDS FOR ARCHLINUX INSTALLS 
ARCHLINUX="base-devel"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},wget http://ftp.gnu.org/gnu/automake/automake-1.15.tar.gz,tar -zxvf automake-1.15.tar.gz,cd automake-1.15,./configure,make,make install,cd ..,rm -rf automake-*,./configure,make,make install"
