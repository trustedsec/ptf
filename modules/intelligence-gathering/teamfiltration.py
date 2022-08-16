#!/usr/bin/env python
#####################################
# Installation module for TeamFiltration
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="David Kennedy (HackingDave)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update TeamFiltration - a cross-platform framework for O365/AAD accounts."

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="FILE"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY - new releases will need to change tag path
REPOSITORY_LOCATION="https://github.com/Flangvik/TeamFiltration/releases/download/v3.3.6/TeamFiltration_Linux"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="teamfiltration"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN=""

# DEPENDS FOR FEDORA INSTALLS
FEDORA=""

# DEPENDS FOR ARCHLINUX INSTALLS
ARCHLINUX=""

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION};chmod +x TeamFiltration_Linux"
