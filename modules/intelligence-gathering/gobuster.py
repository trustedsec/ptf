#!/usr/bin/env python
#####################################
# Installation module for Gobuster
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Zawadi Done" 

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module wil install/update GoBuster" 

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/OJ/gobuster" 

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="gobuster"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="golang" 

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="echo 'export GOPATH=$HOME/go' > ~/.profile, . ~/.profile,go get github.com/OJ/gobuster,cp ~/go/bin/gobuster /usr/local/bin"
