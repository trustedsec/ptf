#!/usr/bin/env python
#####################################
# Installation module for Privilege Escalation Awesome Scripts Suite
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="beyefendi"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update linpeas.sh, winPEAS.exe, winPEAS.bat"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="peas"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git python"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,python"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS=""

# create launcher
LAUNCHER="linpeas"