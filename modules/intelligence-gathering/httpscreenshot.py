#!/usr/bin/env python
#########################################
# Installation module for httpscreenshot
#########################################

# AUTHOR OF MODULE NAME
AUTHOR="Jared Haight (@jaredhaight)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update httpscreenshot, a tool for gathering screenshots of a given list of URLs"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/breenmachine/httpscreenshot"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="httpscreenshot"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git, swig, swig2.0, libssl-dev, python-dev, python-pip"

# COMMANDS TO RUN AFTER 
AFTER_COMMANDS="cd {INSTALL_LOCATION},chmod +x install-dependencies.sh,./install-dependencies.sh,echo '#!/bin/sh' > httpscreenshot,echo 'python {INSTALL_LOCATION}httpscreenshot.py $@' >> httpscreenshot, chmod +x httpscreenshot"

# CREATE LAUNCHER
LAUNCHER="httpscreenshot"
