#!/usr/bin/env python
#####################################
# Installation module for SkipTracer
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="David Kennedy (ReL1K)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update skiptracer - a tool from xillwillx that is an OSINT python webscaping framework"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/xillwillx/skiptracer"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="skiptracer"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,python-pip"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,python-pip"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION}, pip install -r requirements.txt "

# CREATE LAUNCHER
LAUNCHER="skiptracer"



