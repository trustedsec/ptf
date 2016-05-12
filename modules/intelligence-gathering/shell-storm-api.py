#!/usr/bin/env python
#####################################
# Installation module for shell-storm-api
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Mauro Risonho de Paula Assumpcao (firebits)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update shell-storm-api - Search and display all shellcodes in shell-storm database"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/MasterMind555/shell-storm-api.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="shell-storm-api"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git python"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION}"

LAUNCHER="shell-storm-api"
