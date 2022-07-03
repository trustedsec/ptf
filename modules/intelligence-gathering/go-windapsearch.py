#!/usr/bin/env python
#####################################
# Installation module for go-windapsearch
#####################################

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update go-windapsearch a tool to assist in Active Directory Domain enumeration through LDAP queries."

AUTHOR="Ronnie Flathers - ropnop"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/ropnop/go-windapsearch.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="go-windapsearch"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git"

# DEPENDS FOR ARCHLINUX INSTALLS
ARCHLINUX="git,go"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="go get -u github.com/magefile/mage && cd {INSTALL_LOCATION} && mage build"

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER="windapsearch"

# PREREQ INSTALL MODULES NEEDED FOR THIS TOOL TO WORK PROPERLY
TOOL_DEPEND=""
