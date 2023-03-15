#!/usr/bin/env python
#####################################
# Installation module for AMass
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Dave Kennedy (HackingDave)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update AMass - OSINT tool for discovery"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/OWASP/Amass"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="amass"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="snapd"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="snapd"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="systemctl start snapd,snap install amass,export PATH=$PATH:/snap/bin,echo 'export PATH=$PATH:/snap/bin' >> ~/.bashrc,snap refresh amass"

LAUNCHER=""
