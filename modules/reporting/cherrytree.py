#!/usr/bin/env python
#######################################
# Installation module for Cherrytree
#######################################

# AUTHOR OF MODULE NAME
AUTHOR="spinfoo"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update Cherrytree - hierarchical notetaking software"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/giuspen/cherrytree.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="cherrytree"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN=""

# DEPENDS FOR FEDORA INSTALLS
FEDORA=""

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},python setup.py install --prefix={INSTALL_LOCATION}"
