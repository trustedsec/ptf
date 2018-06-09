AUTHOR="Zawadi Done" 

DESCRIPTION="This module wil install/update Gowitness" 

INSTALL_TYPE="GIT"

REPOSITORY_LOCATION="https://github.com/sensepost/gowitness" 

INSTALL_LOCATION="gowitness"

DEBIAN="golang" 

AFTER_COMMANDS="cd {INSTALL_LOCATION},go get -v -u github.com/golang/dep/cmd/dep,cd ~/go/bin, git clone https://github.com/sensepost/gowitness, cd gowitness,dep ensure, go build, mv gowitness /usr/bin/"

LAUNCHER=""
