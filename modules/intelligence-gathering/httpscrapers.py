#!/usr/bin/env python
#########################################
# Installation module for HTTPScrapers
#########################################

# flake8: noqa

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update HTTPScrapers by NetSPI"

AUTHOR="Andrew Schwartz"


# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/NetSPI/HTTPScrapers.git"

#WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="httpscrapers"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,pip3,python3,clousscraper3"

pip3 install cloudscraper

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER="httpscrapers"
