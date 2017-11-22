#!/usr/bin/env python
#####################################
# Installation module for Sublist3r
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Gareth Darby (gazcbm)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update Sublist3r - A Fast subdomains enumeration tool for penetration testers by Ahmed Aboul-Ela"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/aboul3la/Sublist3r"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="sublist3r"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,python-pip"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,python-pip"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION}, pip install -r requirements.txt"

# CREATE LAUNCHER
LAUNCHER="sublist3r"

