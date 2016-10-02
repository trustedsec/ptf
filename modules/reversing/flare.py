#!/usr/bin/env python
#####################################
# Installation module for Flare
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Nick Dyer"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update flare actionscript extractor"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="FILE"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="http://www.nowrap.de/download/flare06linux64.tgz"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="flare"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="tar"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="tar"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},tar -zxvf flare06linux64.tgz,rm flare06linux64.tgz"

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER="flare"
