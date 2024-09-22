#!/usr/bin/env python
#####################################
# Installation module for airgeddon #
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="v1s1t0r1sh3r3"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update airgeddon"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/v1s1t0r1sh3r3/airgeddon"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="airgeddon"

# PREREQ INSTALL MODULES NEEDED FOR THIS TOOL TO WORK PROPERLY
TOOL_DEPEND="modules/wireless/aircrackng"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,iw,awk,pciutils,xterm,procps"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION}, chmod +x airgeddon.sh, ./airgeddon.sh, mv airgeddon.sh airgeddon"

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER="airgeddon"
