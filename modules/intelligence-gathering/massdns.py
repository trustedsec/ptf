AUTHOR="Zawadi Done" 

DESCRIPTION="This module wil install/update MassDNS" 

INSTALL_TYPE="GIT"

REPOSITORY_LOCATION="https://github.com/blechschmidt/massdns" 

INSTALL_LOCATION="massdns" 

DEBIAN="libldns-dev,build-essential,gcc" 

AFTER_COMMANDS="cd {INSTALL_LOCATION},make,cp bin/massdns /usr/local/bin/"

LAUNCHER="massdns" 
