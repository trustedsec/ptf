#!/usr/bin/env python
#####################################
# Installation module for altdns	
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Gareth Darby (gazcbm)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update altdns - A tool that allows for the discovery of subdomains that conform to patterns - by @infosec_au"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/infosec-au/altdns.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="altdns"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,python-pip"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,python-pip"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION}, pip install -r requirements.txt "

# CREATE LAUNCHER
LAUNCHER="altdns"



