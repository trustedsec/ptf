#!/usr/bin/env python
#####################################
# Installation module for Check Hashes
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Andrew Schwartz"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update autoProc by Justn Bollinger (@bandrel) - Tool to check for and reveal AD user accounts that share passwords using a hashdump from a Domain Controller."

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://gist.github.com/3dd47c93cd430606865ec84d281913dc.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="check_hashes"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS=""

LAUNCHER="check_hashes"

# PREREQ INSTALL MODULES NEEDED FOR THIS TOOL TO WORK PROPERLY
TOOL_DEPEND=""
