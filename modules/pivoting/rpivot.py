#!/usr/bin/env python
#####################################
# Installation module for RPIVOT
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="BustedSec (Frank Trezza)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update RPIVOT. It allows you to tunnel traffic into internal networks via socks 4. It works like ssh dynamic port forwarding but in the opposite direction. Example - To start listener on 9999 and make a socks 4 proxy on 127.0.0.1:1080 upon connection from client: python server.py --server-port 9999 --server-ip 0.0.0.0 --proxy-ip 127.0.0.1 --proxy-port 1080"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/artkond/rpivot"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="rpivot"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,make"

# DEPENDS FOR FEDORA INSTALLS
FEDORA=""

# CREATE LAUNCHER
LAUNCHER="client,server"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd /usr/local/bin, sed -i 's/.\/client.py/python client.py/g' client, sed -i 's/.\/server.py/python server.py/g' server"


