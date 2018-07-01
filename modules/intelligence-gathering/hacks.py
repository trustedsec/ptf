AUTHOR="Zawadi Done" 

DESCRIPTION="This module wil install/update some random scripts" 

INSTALL_TYPE="GIT"

REPOSITORY_LOCATION="https://github.com/EdOverflow/hacks" 

INSTALL_LOCATION="hacks"

DEBIAN="" 

AFTER_COMMANDS="cd {INSTALL_LOCATION},cd .., cp -R hacks/. /usr/local/bin/"

