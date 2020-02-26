#!/usr/bin/env python
#####################################
# Installation module for Turbolist3r
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Zawadi Done" 

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module wil install/update Turbolist3r" 

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/fleetcaptain/Turbolist3r" 

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="turbolist3r"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="python,python-pip,python-requests" 

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION}, pip install -r requirements.txt, chmod +x turbolist3r.py"

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER="turbolist3r"
