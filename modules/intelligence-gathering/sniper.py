#!/usr/bin/env python
#####################################
# Installation module for SN1PER
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="David Kennedy (ReL1K)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update SN1PER - tool for recon."

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/1N3/Sn1per"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="sniper"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git xprobe2 whois curl nmap cutycapt host php php-curl"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},chmod +x install.sh,echo -e "y\n" | ./install.sh,chmod +x sniper"

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER="sniper"

# NEED THIS TO RUN INSTALL TO UPDATE EVERYTHING
BYPASS_UPDATE="YES"
