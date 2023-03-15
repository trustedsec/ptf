#!/usr/bin/env python
#####################################
# Installation module for goofile
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Jason Ashton (ninewires)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update goofile - a Google Advanced Searches tool"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="WGET"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/goofile/goofilev1.5.zip"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="goofile"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN=""

# DEPENDS FOR FEDORA INSTALLS
FEDORA=""

# COMMANDS TO RUN AFTER 
AFTER_COMMANDS="cd {INSTALL_LOCATION}, unzip goofilev1.5.zip, mv goofilev1.5/* ., rm -rf goofilev1.5/, rm goofilev1.5.zip"

# create a launcher
LAUNCHER="goofile"
