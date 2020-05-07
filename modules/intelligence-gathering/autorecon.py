#####################################
# Installation module for autorecon
#####################################

# XXX: Expects seclists to be in /usr/share/seclists

# AUTHOR OF MODULE NAME
AUTHOR="ypcrts"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update autorecon - a multi-threaded network reconnaissance tool"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/Tib3rius/AutoRecon.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="autorecon"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="python3,python3-pip"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION}, pip3 install -r requirements.txt"

# AUTOMATIC LAUNCH
LAUNCHER="autorecon"

# needed for install
#BYPASS_UPDATE="YES"
