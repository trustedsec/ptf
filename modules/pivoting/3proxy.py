#!/usr/bin/env python
#####################################
# Installation module for 3proxy
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="BustedSec (Frank Trezza)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update 3proxy. This tool the swiss army knife of the  proxy world and has a lot of functionality. Useful as a socks proxy or port forwarder. This tool gets all of its options from a config file. To run it use syntax 3proxy config_file: with something like 'socks -p1080' inside the config file.  "

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/z3APA3A/3proxy"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="3proxy"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,make"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,make"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},make -f Makefile.Linux,cd src, install 3proxy {INSTALL_LOCATION}, touch 3proxy.cfg "

# CREATE LAUNCHER
LAUNCHER="3proxy"
