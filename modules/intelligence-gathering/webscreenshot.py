AUTHOR="Zawadi Done" 

DESCRIPTION="This module wil install/update webscreenshot" 

INSTALL_TYPE="GIT"

REPOSITORY_LOCATION="https://github.com/maaaaz/webscreenshot" 

INSTALL_LOCATION="webscreenshot"

DEBIAN="phantomjs" 

AFTER_COMMANDS="cd {INSTALL_LOCATION}, pip install webscreenshot, npm install express-photo-gallery"

LAUNCHER="webscreenshot"
