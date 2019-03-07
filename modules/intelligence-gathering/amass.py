AUTHOR="Zawadi Done"

DESCRIPTION="This module wil install/update amass"

INSTALL_TYPE="GIT"

REPOSITORY_LOCATION="https://github.com/OWASP/Amass"

INSTALL_LOCATION="amass"

DEBIAN="snapd"

AFTER_COMMANDS="export GOPATH=$HOME/go,systemctl start snapd,snap install amass, echo 'You need to reboot before using Amass', sleep 5"
