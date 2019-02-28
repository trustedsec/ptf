#!/usr/bin/env python
#####################################
# Installation module for Gitrob
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Zawadi Done" 

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module wil install/update Gitrob" 

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/michenriksen/gitrob" 

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="gitrob"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="golang" 

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="export GOPATH=$HOME/go,go get github.com/michenriksen/gitrob,cp ~/go/bin/gitrob /usr/local/bin"
