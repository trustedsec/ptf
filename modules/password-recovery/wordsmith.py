#!/usr/bin/env python
#####################################
# Installation module for Wordsmith
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Sanjiv Kawa (@skawasec)" 

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update Wordsmith, a tailored wordlist generator based on geo-location"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/skahwah/wordsmith.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="wordsmith"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git ruby"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git ruby"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION}, bundle install"