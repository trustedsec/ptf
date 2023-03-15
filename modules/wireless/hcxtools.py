#!/usr/bin/env python
#####################################
# Installation module for hcxtools
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Corey Batiuk (skapunker)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update hcxtools - tools for converting and analyzing wireless captures"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/ZerBea/hcxtools.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="hcxtools"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,build-essential"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,make,gcc"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},make,make install"

LAUNCHER="hcxcapngtool,hcxhashtool,hcxpsktool,hcxeiutool,hcxwltool,hcxhash2cap,wlancap2wpasec,whoismac"

BYPASS_UPDATES="YES"
