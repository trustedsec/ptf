#!/usr/bin/env python
#####################################
# Installation module for Subfinder
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Zawadi Done" 

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module wil install/update Subfinder" 

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="github.com/Ice3man543/subfinder" 

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="subfinder"

# WHERE DO YOU WANT TO INSTALL IT
DEBIAN="golang" 

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="echo 'export GOPATH=$HOME/go' > ~/.profile, . ~/.profile,go get -u github.com/Ice3man543/subfinder,cp ~/go/bin/subfinder /usr/local/bin/"
