#!/usr/bin/env python
#####################################
# Installation module for cfr
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Jens Muecke (ryd)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update cfr, a tool for decompiling java classes"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="FILE"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="http://www.benf.org/other/cfr/cfr_0_110.jar" 

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="cfr"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="default-jdk"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="java-1.8.0-openjdk"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},printf '#!/bin/sh\njava -jar %s%s\n' '{INSTALL_LOCATION}' 'cfr_0_110.jar'>cfr,chmod o+x cfr"

LAUNCHER="cfr"
