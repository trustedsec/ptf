#!/usr/bin/env python
#######################################
# Installation module for mana-toolkit
#######################################

# AUTHOR OF MODULE NAME
AUTHOR="jklaz"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update the mana-toolkit"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/sensepost/mana"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="mana"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="libnl-3-dev,isc-dhcp-server,tinyproxy,libssl-dev,apache2,macchanger,python-dnspython,python-pcapy,dsniff,stunnel4,python-scapy"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,libnl,dhcp-forwarder,tinyproxy,openssl,httpd,macchanger,python-dns,pcapy,dsniff,stunnel,scapy,sslsplit"

#In order to check new versions of sslstrip+ and net-creds
BYPASS_UPDATE="YES"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="git clone --depth 1 https://github.com/sensepost/mana {INSTALL_LOCATION},cd {INSTALL_LOCATION},git submodule init,git submodule update,make,make install"
