#!/usr/bin/env python
#####################################
# Installation module for EMPIRE
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Jared Haight (@jaredhaight)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update Empire - A Powershell based post-explotation framework"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/powershellempire/empire"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="empire"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git, python-m2crypto, python-crypto"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,m2crypto,python-crypto"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},cd setup,echo -e "\n" | ./install.sh"

# DONT RUN AFTER COMMANDS ON UPDATE
BYPASS_UPDATE=YES

# LAUNCHER
LAUNCHER="empire"
