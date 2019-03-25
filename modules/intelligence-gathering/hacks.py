AUTHOR="Zawadi Done" 

DESCRIPTION="This module wil install/update some random scripts" 

INSTALL_TYPE="GIT"

REPOSITORY_LOCATION="https://github.com/EdOverflow/hacks" 

INSTALL_LOCATION="hacks"

DEBIAN="git" 

AFTER_COMMANDS="cd {INSTALL_LOCATION}, rm LICENSE README LICENSE, cp -r * /usr/local/bin/"

