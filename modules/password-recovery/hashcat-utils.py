#!/usr/bin/env python
#####################################
# Installation module for Hashcat-Utils
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Martin Bos (@purehate_)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update Hashcat-Utils - Small utilities that are useful in advanced password cracking"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/hashcat/hashcat-utils.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="hashcat-utils"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION}src/, make linux"


# DONT RUN AFTER COMMANDS ON UPDATE
BYPASS_UPDATE=NO

# LAUNCHER
LAUNCHER="hashcat-utils"

