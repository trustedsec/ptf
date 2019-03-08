#!/usr/bin/env python
#####################################
# Installation module for SubOver
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Zawadi Done" 

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module wil install/update SubOver" 

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/Ice3man543/SubOver" 

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="subover"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="golang" 

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="echo 'export GOPATH=$HOME/go' > ~/.profile, . ~/.profile,go get github.com/Ice3man543/SubOver,cp ~/go/bin/SubOver /usr/local/bin/subover"
