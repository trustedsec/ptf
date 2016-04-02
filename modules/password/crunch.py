#!/usr/bin/env python
#####################################
# Installation module for pyobfuscate
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="jklaz"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update crunch - wordlist generator"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="FILE"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://downloads.sourceforge.net/project/crunch-wordlist/crunch-wordlist/crunch-3.6.tgz"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="crunch"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="gcc"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="gcc"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},tar -xf crunch-3.6.tgz,cd crunch-3.6,make,make install"
