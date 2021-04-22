#!/usr/bin/env python
#####################################
# Installation module for EMPIRE
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Jared Haight (@jaredhaight) and Jeff McJunkin (@jeffmcjunkin)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update Empire and Deathstar - A PowerShell-based post-exploitation framework"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/BC-SECURITY/Empire/"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="empire-ps"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git, python-m2crypto, python-crypto, python3-pip, python-dev, libxml2-dev, libssl-dev, libz-dev, make"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,m2crypto,python-crypto"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS='cd {INSTALL_LOCATION},pip3 install poetry,./setup/install.sh,git clone https://github.com/byt3bl33d3r/DeathStar,cd DeathStar,python3 -m pip install --user pipx,poetry install'

# DON'T RUN AFTER COMMANDS ON UPDATE
BYPASS_UPDATE="YES"

# LAUNCHER
LAUNCHER="empire"
