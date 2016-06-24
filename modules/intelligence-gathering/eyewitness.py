#!/usr/bin/env python
#######################################
# Installation module for eyewitness
#######################################

# AUTHOR OF MODULE NAME
AUTHOR="Kirk Hayes (l0gan)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update EyeWitness."

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/ChrisTruncer/EyeWitness"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="eyewitness"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,python-setuptools,libffi-dev,libssl-dev"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION}/setup,./setup.sh,cd /tmp,wget -O phantomjs.tar.bz2 https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2,tar -xf phantomjs.tar.bz2,cp phantomjs-2.1.1-linux-x86_64/bin/phantomjs {INSTALL_LOCATION}/bin/phantomjs"
