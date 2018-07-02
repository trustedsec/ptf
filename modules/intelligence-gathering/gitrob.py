AUTHOR="Zawadi Done" 

DESCRIPTION="This module wil install/update Gitrob" 

INSTALL_TYPE="GIT"

REPOSITORY_LOCATION="https://github.com/michenriksen/gitrob" 

INSTALL_LOCATION="gitrob"

DEBIAN="golang" 

AFTER_COMMANDS="cd {INSTALL_LOCATION}, go get github.com/michenriksen/gitrob,cp ~/go/bin/gitrob /usr/local/bin"
