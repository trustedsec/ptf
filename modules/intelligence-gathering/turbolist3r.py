AUTHOR="Zawadi Done" 

DESCRIPTION="This module wil install/update Turbolist3r" 


INSTALL_TYPE="GIT"


REPOSITORY_LOCATION="https://github.com/fleetcaptain/Turbolist3r" 

INSTALL_LOCATION="turbolist3r"

DEBIAN="python-requests" 

AFTER_COMMANDS="cd {INSTALL_LOCATION}, pip install -r requirements.txt"

LAUNCHER="turbolist3r"
