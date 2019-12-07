#!/usr/bin/env python
#####################################
# Installation module for DirbPy
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Sabe Barker (sabebarker)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update DirbPy - A new version of dirb in python by Marc-Olivier Bouchard"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/marcolivierbouch/dirbpy.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="dirbpy"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,python3,python3-pip"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,python3,python3-pip" # ToDo

# BYPASS UPDATES
BYPASS_UPDATE="NO"

# COMMANDS TO RUN AFTER 
AFTER_COMMANDS="cd {INSTALL_LOCATION},pip3 install -r requirements.txt,python3 setup.py install"

