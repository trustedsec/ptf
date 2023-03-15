#!/usr/bin/env python
#####################################
# Installation module for pyobfuscate
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Justin Herman (JDogHerman)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update pyobfuscate"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/astrand/pyobfuscate"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="pyobfuscate"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},python setup.py install"
LAUNCHER="pyobfuscate"

