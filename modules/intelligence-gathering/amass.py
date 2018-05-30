AUTHOR="Zawadi Done" 

DESCRIPTION="This module wil install/update amass" 

INSTALL_TYPE="GIT"

REPOSITORY_LOCATION="https://github.com/caffix/amass" 

INSTALL_LOCATION="amass"

DEBIAN="snapd" 

AFTER_COMMANDS="cd /root/go/bin,go get -u github.com/caffix/amass,mv amass /usr/bin/"

