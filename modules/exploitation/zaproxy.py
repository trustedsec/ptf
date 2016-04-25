#!/usr/bin/env python
#####################################
# Installation module for zaproxy
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="David Kennedy (ReL1K)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update the Burp Suite Free - web application attacks"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="WGET"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY - do not change zaproxy for repository location - do magic in the background to pull latest version
REPOSITORY_LOCATION="zaproxy"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="zap"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="default-jre"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="java-1.8.0-openjdk"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},tar zxvf ZAP_*,rm *.tar.gz,cp -rf ZAP_*/* ./,rm -rf ZAP_*"

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER="zap"

# BYPASS UPDATE
BYPASS_UPDATE="YES"

