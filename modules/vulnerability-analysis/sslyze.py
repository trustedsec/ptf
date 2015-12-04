#!/usr/bin/env python
#####################################
# Installation module for SSLyze
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Jason Ashton (@jayw0k)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update SSLyze - an SSL configuration analyzer"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/nabla-c0d3/sslyze.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="sslyze"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="unzip"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="unzip"

# DEPENDS FOR ARCHLINUX INSTALLS
ARCHLINUX="unzip"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION}, wget https://github.com/nabla-c0d3/sslyze/releases/download/release-0.12/sslyze-0_12-linux64.zip, unzip sslyze-0_12-linux64.zip && rm -rf sslyze-0_12-linux64.zip, mv sslyze/nassl ., rm -rf sslyze"
	
# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER="sslyze"
