AUTHOR="Zawadi Done"

DESCRIPTION="This module will install/update Passhunt"

INSTALL_TYPE="GIT"

REPOSITORY_LOCATION="https://github.com/Viralmaniar/Passhunt"

INSTALL_LOCATION="passhunt"

DEBIAN="git,python3,python3-pip"

AFTER_COMMANDS="cd {INSTALL_LOCATION},pip3 install -r requirements.txt"

LAUNCHER="passhunt"
