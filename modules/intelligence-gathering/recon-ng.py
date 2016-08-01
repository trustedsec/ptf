#!/usr/bin/env python
#####################################
# Installation module for recon-ng
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="David Kennedy (ReL1K)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update Recon-NG - a recon tool" 

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://bitbucket.org/LaNMaSteR53/recon-ng/"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="recon-ng"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git python python-xlsxwriter python-crypto python-mechanize python-pip"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,python,python-crypto,python-mechanize"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="python -m pip install --upgrade pip,python -m pip install dicttoxml PyPDF2,cd {INSTALL_LOCATION},pip install -r REQUIREMENTS"

# CREATE LAUNCHER
LAUNCHER="recon-ng"

BYPASS_UPDATE="YES"
