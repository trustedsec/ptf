AUTHOR="Zawadi Done"

DESCRIPTION="This module wil install/update amass"

INSTALL_TYPE="GIT"

REPOSITORY_LOCATION="https://github.com/OWASP/Amass"

INSTALL_LOCATION="amass"

DEBIAN="snapd"

AFTER_COMMANDS="systemctl start snapd,export PATH=$PATH:/snap/bin,snap refresh,snap install amass"
