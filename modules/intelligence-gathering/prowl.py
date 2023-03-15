#!/usr/bin/env python
#####################################
# Installation module for prowl
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Nick Dyer"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update Nettitude's Prowl by @MattSPickford - LinkedInCrawler"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/nettitude/Prowl.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="prowl"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="python python-pip"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION} && pip install -r requirements.txt"

# CREATE LAUNCHER
LAUNCHER="prowl"
