#!/usr/bin/env python
#####################################
# Installation module for Snoopy-NG
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Dave Kennedy (HackingDave)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update Snoopy-NG - modular digital terrestrial tracking framework"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/sensepost/snoopy-ng" 

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="snoopy-ng"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},sh install.sh, apt-get install --force-yes --yes python-setuptools autossh python-psutil python2.7-dev libpcap0.8-dev ppp tcpdump python-serial sqlite3 python-requests iw build-essential python-bluez python-flask python-gps python-dateutil python-dev python-libpcap libxml2-dev libxslt-dev pyrit mitmproxy"
