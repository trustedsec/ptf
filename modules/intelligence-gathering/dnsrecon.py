#!/usr/bin/env python
#####################################
# Installation module for DNSRecon
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Greg Hetrick (gchetrick)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update dnsrecon - a dns enum tool by Carlos Parez"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/darkoperator/dnsrecon"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="dnsrecon"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,python-pip"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,python-pip"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},pip install -r requirements.txt"

# CREATE LAUNCHER
LAUNCHER="dnsrecon"

