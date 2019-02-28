#!/usr/bin/env python
#####################################
# Installation module for Password Analysis and Cracking Kit (PACK)
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Larry Spohn (Spoonman)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update PACK - a collection of utilities designed for advanced cracking with hashcat"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="FILE"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="http://thesprawl.org/media/projects/PACK-0.0.4.tar.gz"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="pack"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="libenchant1c2a"

# DEPENDS FOR FEDORA INSTALLS
FEDORA=""

# DON'T RUN AFTER COMMANDS ON UPDATE
BYPASS_UPDATE="NO"

# COMMANDS TO RUN AFTER 
AFTER_COMMANDS="cd {INSTALL_LOCATION},tar xzf PACK-0.0.4.tar.gz --strip 1,rm PACK-0.0.4.tar.gz"
