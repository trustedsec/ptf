#!/usr/bin/env python
#####################################
# Installation module for discover
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Martin Bos (purehate)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update discover - an OSINT tool"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/leebaird/discover.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="discover"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git, whois, traceroute, whatweb, arp-scan, cutycapt, gnumeric"

# COMMANDS TO RUN AFTER 
AFTER_COMMANDS="pip install urllib3[secure] --upgrade"

# CREATE LAUNCHER
LAUNCHER="discover"
