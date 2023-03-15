#!/usr/bin/env python
#####################################
# Installation module for Cowpatty
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="willhackforsushi"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update Cowpatty - offline dictionary attack against WPA/WPA2 networks using PSK-based authentication"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="FILE"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="http://www.willhackforsushi.com/code/cowpatty/4.6/cowpatty-4.6.tgz"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="cowpatty"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="libssl-dev libpcap-dev"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},tar zxfv cowpatty-4.6.tgz,rm -rf *.tgz,cd cowpatty-4.6,make -j4,sudo cp cowpatty /usr/bin"

# LAUNCHER
LAUNCHER="cowpatty"
