#!/usr/bin/env python
#####################################
# Installation module for DomainCheck
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Andrew Schwartz"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update DomainCheck by Christopher Maddalena (@cmaddy) - A tool to help monitor changes related to their domain names. This includes negative changes in categorization, VirusTotal detections, and appearances on malware blacklists."

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/GhostManager/DomainCheck"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="domaincheck"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git"

# create a launcher
LAUNCHER="domaincheck"
