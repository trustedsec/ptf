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
REPOSITORY_LOCATION="https://github.com/lanmaster53/recon-ng"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="recon-ng"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git python3 python3-pip"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,python3,python3-pip"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="pip3 install PyPDF3 pyaes bs4,cd {INSTALL_LOCATION},pip3 install -r REQUIREMENTS"

# CREATE LAUNCHER
LAUNCHER="recon-ng"

BYPASS_UPDATE="YES"
