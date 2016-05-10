#!/usr/bin/env python
#####################################
# Installation module for crunch
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="jklaz"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update crunch - wordlist generator"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE ,wget
INSTALL_TYPE="wget"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://downloads.sourceforge.net/project/crunch-wordlist/crunch-wordlist/crunch-3.6.tgz"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="crunch"

#not github program manual update of the link needed
BYPASS_UPDATE="YES"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="wget gcc"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="gcc"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},tar -xf crunch-3.6.tgz,cd crunch-3.6,make,make install,cd ..,rm crunch-3.6.tgz,cp crunch-3.6/crunch ./"

LAUNCHER="crunch"
