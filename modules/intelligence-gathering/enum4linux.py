#!/usr/bin/env python
#####################################
# Installation module for Enum4Linux
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Corey Batiuk (skapunker)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update enum4linux."

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/CiscoCXSecurity/enum4linux.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="enum4linux"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,perl,smbclient"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,perl,samba-client"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="wget https://raw.githubusercontent.com/Wh1t3Fox/polenum/master/polenum.py -O /usr/local/bin/polenum, chmod +x /usr/local/bin/polenum"

# CREATE LAUNCHER
LAUNCHER="enum4linux"

# PREREQ INSTALL MODULES NEEDED FOR THIS TOOL TO WORK PROPERLY
TOOL_DEPEND="modules/exploitation/impacket"
