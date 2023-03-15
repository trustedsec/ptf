#!/usr/bin/env python
#####################################
# Installation module for onedrive_user_enum
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Matt (hostess) Andreko"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update onedrive_user_enum - a user enumeration tool for MS OneDrive"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/nyxgeek/onedrive_user_enum.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="onedrive_user_enum"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,python-pip"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,python-pip"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},pip install requests"

# CREATE LAUNCHER
LAUNCHER="onedrive_user_enum"

