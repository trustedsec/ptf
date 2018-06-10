AUTHOR="Zawadi Done" 

DESCRIPTION="This module wil install/update SubOver" 

INSTALL_TYPE="GIT"

REPOSITORY_LOCATION="https://github.com/Ice3man543/SubOver" 

INSTALL_LOCATION="subover"

DEBIAN="golang" 

AFTER_COMMANDS="cd ~/go/bin/,go get github.com/Ice3man543/SubOver, mv SubOver /usr/local/bin/subover"
