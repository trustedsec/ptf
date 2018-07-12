#!/usr/bin/env python
#####################################
# Installation module for msfenum
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Wesley Neelen (@wez3forsec)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update msfenum - A Metasploit auto auxiliary script"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/wez3/msfenum/"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="msfenum"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="chmod 766 {INSTALL_LOCATION}/msfenum.log, chmod 777 {INSTALL_LOCATION}/logs"

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER="msfenum"

# PREREQ INSTALL MODULES NEEDED FOR THIS TOOL TO WORK PROPERLY
TOOL_DEPEND="modules/exploitation/metasploit"
