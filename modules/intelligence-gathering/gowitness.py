#!/usr/bin/env python
#####################################
# Installation module for Gowitness
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Zawadi Done" 

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module wil install/update Gowitness" 

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/sensepost/gowitness" 


# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="gowitness"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="golang" 

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="export GOPATH=$HOME/go,go get -u github.com/golang/dep/cmd/dep,cp ~/go/bin/dep /usr/local/bin/,cd /root/go/src,git clone https://github.com/sensepost/gowitness .,cd gowitness,dep ensure -update,make,cd build,cp gowitness-linux-amd64 gowitness,cp /root/go/src/gowitness/build/gowitness /usr/local/bin/,cd {INSTALL_LOCATION},wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb, dpkg -i google-chrome-stable_current_amd64.deb, apt install -f -y, dpkg -i google-chrome-stable_current_amd64.deb, rm google-chrome-stable_current_amd64.deb"
