#!/usr/bin/env python
#####################################
# Installation module for Enum4Linux
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Steven van der Baan (vdbaan)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update enum4linux (Portcullis Labs)."

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/portcullislabs/enum4linux.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="enum4linux"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,perl"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,perl"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION}, wget https://labs.portcullis.co.uk/download/polenum-0.2.tar.bz2, tar -xjvf polenum-0.2.tar.bz2; rm polenum-0.2.tar.bz2, mv polenum-0.2/polenum.py /usr/bin/, rm -rf polenum-0.2"

# CREATE LAUNCHER
LAUNCHER="enum4linux"
