#!/usr/bin/env python
#####################################
# Installation module for Veil-Framework
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Nick Dyer"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update Veil-Framework"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/Veil-Framework/Veil.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="veil-framework"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git python-pycryptopp python-capstone"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="python-pycryptopp python-capstone"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION}, ./Install.sh -c, ln -s {INSTALL_LOCATION}Veil-Evasion/Veil-Evasion.py /usr/local/bin/Veil-Evasion, ln -s {INSTALL_LOCATION}Veil-Catapult/Veil-Catapult.py /usr/local/bin/Veil-Catapult, ln -s {INSTALL_LOCATION}veil-framework/Veil-Pillage/Veil-Pillage.py /usr/local/bin/Veil-Pillage, ln -s {INSTALL_LOCATION}veil-framework/Veil-Ordnance/Veil-Ordnance.py /usr/local/bin/Veil-Ordnance"

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER=""
