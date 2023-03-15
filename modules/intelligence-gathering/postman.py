#!/usr/bin/env python
#######################################
# Installation module for PostMan
#######################################

# AUTHOR OF MODULE NAME
AUTHOR="Manuel Gines (xkulio)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install PostMan"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE, WGET
INSTALL_TYPE="WGET"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://dl.pstmn.io/download/latest/linux32"

#X64 LOCATION
X64_LOCATION="https://dl.pstmn.io/download/latest/linux64"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="postman"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="wget libgconf-2-4"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="" # ToDo

# BYPASS UPDATES
BYPASS_UPDATE="YES"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},mv linux64 postman64.tar.gz,tar -xzf postman64.tar.gz,mv Postman Install,mv Install/* .,rm -Rf Install postman64.tar.gz,rm /usr/local/bin/postman,ln -s {INSTALL_LOCATION}/app/Postman /usr/local/bin/postman"

# CREATE LAUNCHER
LAUNCHER="postman"
