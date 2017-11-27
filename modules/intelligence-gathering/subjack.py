#!/usr/bin/env python
#####################################
# Installation module for Sublist3r
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Gareth Darby (gazcbm)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update Subjack - A Hostile Subdomain Takeover tool written in Go by Haccer"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/haccer/subjack.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="subjack"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,golang"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,golang"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION}, go build subjack.go"

# CREATE LAUNCHER
LAUNCHER="subjack"

