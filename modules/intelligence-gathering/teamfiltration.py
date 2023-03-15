#!/usr/bin/env python
#####################################
# Installation module for TeamFiltration
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="David Kennedy (HackingDave)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update TeamFiltration - a cross-platform framework for O365/AAD accounts."

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD, TAGS
# OPTIONS = GIT, SVN, FILE, TAGS
INSTALL_TYPE="TAGS"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY - new releases will need to change tag path
REPOSITORY_LOCATION=""

# IF INSTALL_TYPE TAGS IS SPECIFIED, THIS WILL PULL THE LATEST VERSION OF AN APPLICATION BACK VIA GITHUB TAGS
# YOU WILL NEED TO KNOW THE OWNER, REPO, AND FILENAME. EXAMPLE: https://github.com/Flangvik/TeamFiltration/
# THE OWNER: FLANGVIK
# THE REPO: TeamFiltration
# THE FILENAME CAN BE FOUND UNDER https://github.com/Flangvik/TeamFiltration/releases/
# IN THIS EXAMPLE TeamFiltration_Linux IS THE NAME OF THE FILE WE ARE DOWNLOADING

# OWNER OF THE REPO
OWNER="FLANGVIK"

# REPO NAME FOR THE TOOL/PROJECT
REPOHOME="TeamFiltration"

# FILENAME WE ARE DOWNLOADING
FILENAME="TeamFiltration_Linux"

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
