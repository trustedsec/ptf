#!/usr/bin/env python
#####################################
# Installation module for dnstwist
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Jason Ashton (ninewires)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update dnstwist - Domain name permutation engine for detecting homograph phishing attacks, typo squatting, and brand impersonation"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION=""

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="dnstwist"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,python-pip,python3-dnspython python3-tld python3-geoip python3-whois python3-requests python3-ssdeep"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,python-pip"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},python3 -m pip install -r requirements.txt"

# CREATE LAUNCHER
LAUNCHER="dnstwist"

