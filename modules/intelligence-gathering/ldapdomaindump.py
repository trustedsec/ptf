#!/usr/bin/env python
#########################################
# Installation module for LDAPDomainDump
#########################################

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update LDAPDomainDump a Active Directory information dumper via LDAP"

AUTHOR="Andrew Schwartz"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/dirkjanm/ldapdomaindump.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="ldapdomaindump"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,python3-ldap3, python3-dnspython"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,python3-ldap3, python3-dnspython"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},python setup.py install"

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER="ldapdomaindump"

# PREREQ INSTALL MODULES NEEDED FOR THIS TOOL TO WORK PROPERLY
TOOL_DEPEND=""
