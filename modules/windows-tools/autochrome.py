AUTHOR="Zawadi Done" 

DESCRIPTION="This module wil install/update Autochrome" 

INSTALL_TYPE="GIT"

REPOSITORY_LOCATION="https://github.com/nccgroup/autochrome" 

INSTALL_LOCATION="autochrome"

DEBIAN="unzip, ruby" 

AFTER_COMMANDS="cd {INSTALL_LOCATION}, ruby autochrome.rb"

LAUNCHER=""
