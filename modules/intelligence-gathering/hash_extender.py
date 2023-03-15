#!/usr/bin/env python
#####################################
# Installation module for hash_extender
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Jeff McJunkin (@jeffmcjunkin)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install hash_extender, a tool for doing hash length extension attacks"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/iagox86/hash_extender.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="hash_extender"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="build-essential openssl"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},make"

# DON'T RUN AFTER COMMANDS ON UPDATE
BYPASS_UPDATE="NO"

# LAUNCHER
LAUNCHER="hash_extender"
