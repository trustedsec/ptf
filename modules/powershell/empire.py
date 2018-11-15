#!/usr/bin/env python
#####################################
# Installation module for EMPIRE
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Jared Haight (@jaredhaight)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update Empire and Deathstar - A Powershell based post-exploitation framework"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/EmpireProject/Empire"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="empire-ps"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git, python-m2crypto, python-crypto, python3-pip, python-dev, libxml2-dev, libssl1.0-dev, libz-dev, make"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,m2crypto,python-crypto"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS='cd {INSTALL_LOCATION},cd setup,echo -e "\n" | ./install.sh,git clone https://github.com/byt3bl33d3r/DeathStar,cd DeathStar,git pull,pip3 install -r requirements.txt'

# DON'T RUN AFTER COMMANDS ON UPDATE
BYPASS_UPDATE="YES"

# LAUNCHER
LAUNCHER="empire"
