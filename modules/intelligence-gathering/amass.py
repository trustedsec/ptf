AUTHOR="Zawadi Done" 

DESCRIPTION="This module wil install/update amass" 

INSTALL_TYPE="GIT"

REPOSITORY_LOCATION="https://github.com/caffix/amass" 

INSTALL_LOCATION="amass"

DEBIAN="golang" 

AFTER_COMMANDS="cd ~/go/bin,go get -u github.com/caffix/amass,cp amass /usr/local/bin/"

