AUTHOR="Zawadi Done" 

DESCRIPTION="This module wil install/update GoBuster" 

INSTALL_TYPE="GIT"

REPOSITORY_LOCATION="https://github.com/OJ/gobuster" 

INSTALL_LOCATION="gobuster"

DEBIAN="golang" 

AFTER_COMMANDS="go get github.com/OJ/gobuster,cp /root/go/bin/gobuster /usr/local/bin"

LAUNCHER=""
