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


# WHERE DO YOU WANT TO INSTALL ITexi
INSTALL_LOCATION="gowitness"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="golang,wget,curl" 

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="echo 'export GOPATH=$HOME/go' > ~/.profile, . ~/.profile,cp ~/go/bin/dep /usr/local/bin,curl https://raw.githubusercontent.com/golang/dep/master/install.sh | sh,cd ~/go/src,cd {INSTALL_LOCATION},dep ensure -update,make,cd build,cp gowitness-linux-amd64 gowitness,cp gowitness /usr/local/bin/,cd {INSTALL_LOCATION},wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb, dpkg -i google-chrome-stable_current_amd64.deb, apt install -f -y, dpkg -i google-chrome-stable_current_amd64.deb, rm google-chrome-stable_current_amd64.deb"
