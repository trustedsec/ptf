AUTHOR="Zawadi Done" 

DESCRIPTION="This module wil install/update Gowitness" 

INSTALL_TYPE="GIT"

REPOSITORY_LOCATION="https://github.com/sensepost/gowitness" 

INSTALL_LOCATION="gowitness"

DEBIAN="golang" 

AFTER_COMMANDS="cd {INSTALL_LOCATION},go get -v -u github.com/golang/dep/cmd/dep,cd ~/go/src, git clone https://github.com/sensepost/gowitness, cd gowitness,dep ensure, go build, cp gowitness /usr/local/bin/, wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb, dpkg -i google-chrome-stable_current_amd64.deb, apt install -f, dpkg -i google-chrome-stable_current_amd64.deb, rm *.deb"

LAUNCHER=""

