#!/usr/bin/env python
#####################################
# Installation module for Flasm
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Nick Dyer"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update flasm a command line Flash assembler/disassembler."

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="FILE"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="http://www.nowrap.de/download/flasm16linux.tgz"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="flasm"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="tar"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="tar"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},tar -zxvf flasm16linux.tgz,rm flasm16linux.tgz"

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER="flasm"
