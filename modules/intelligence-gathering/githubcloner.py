#!/usr/bin/env python
#####################################
# Installation module for GithubCloner
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Mazin Ahmed (mazen160)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update GithubCloner"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/mazen160/GithubCloner.git"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="python"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="python"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="githubcloner"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION} ; pip install -r requirements.txt"

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER="githubcloner"
