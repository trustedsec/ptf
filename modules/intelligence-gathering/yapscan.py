#!/usr/bin/env python
#####################################
# Installation module for YapScan
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Steven van der Baan (vdbaan)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update yapscan (Pentest Monkey)."

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/pentestmonkey/yapscan.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="yapscan"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,gcc,make"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,gcc,make"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},make,make install"

LAUNCHER="yapscan"
