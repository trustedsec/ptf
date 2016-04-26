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
DEBIAN="python-pycryptopp python-capstone"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="python-pycryptopp python-capstone"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION}, ./Install.sh -c, ln -s {INSTALL_LOCATION}Veil-Evasion/Veil-Evasion.py /usr/local/bin/Veil-Evasion.py, ln -s {INSTALL_LOCATION}Veil-Catapult/Veil-Catapult.py /usr/local/bin/Veil-Catapult.py, ln -s {INSTALL_LOCATION}veil-framework/Veil-Pillage/Veil-Pillage.py /usr/local/bin/Veil-Pillage.py.py, ln -s {INSTALL_LOCATION}veil-framework/Veil-Ordnance/Veil-Ordnance.py /usr/local/bin/Veil-Ordnance.py"

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER=""
