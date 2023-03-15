#!/usr/bin/env python
#####################################
# Installation module for Password Analysis and Cracking Kit (PACK)
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Sabe Barker"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update PACK - a collection of utilities designed for advanced cracking with hashcat"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/Hydraze/pack.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="pack"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="libenchant1c2a,python3-enchant"

# DEPENDS FOR FEDORA INSTALLS
FEDORA=""

# DON'T RUN AFTER COMMANDS ON UPDATE
BYPASS_UPDATE="NO"

# COMMANDS TO RUN AFTER 
AFTER_COMMANDS="cd {INSTALL_LOCATION},ln -s {INSTALL_LOCATION}maskgen.py /usr/bin/maskgen,ln -s {INSTALL_LOCATION}policygen.py /usr/bin/policygen,ln -s {INSTALL_LOCATION}rulegen.py /usr/bin/rulegen,ln -s {INSTALL_LOCATION}statsgen.py /usr/bin/statsgen"
