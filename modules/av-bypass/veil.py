#!/usr/bin/env python
#####################################
# Installation module for veil
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Justin Herman (JDogHerman)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update veil"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/Veil-Framework/Veil"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="veil"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN=""

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},export DEBIAN_FRONTEND=noninteractive,echo y | ./Install.sh -c"
