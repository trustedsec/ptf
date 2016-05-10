#!/usr/bin/env python
#####################################
# Installation module for sap-dissector-wireshark
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Mauro Risonho de Paula Assumpcao (firebits)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update sap-dissector-wireshark - This Wireshark plugin provides dissection of SAP's NI, Message Server, Router, Diag and Enqueue protocols."

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/CoreSecurity/SAP-Dissection-plug-in-for-Wireshark.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="sap-dissector-wireshark"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,python,wireshark,wireshark-dev,cmake, make"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,wireshark,wireshark-devel,cmake,make"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},mkdir build,cd build,cmake ..,make,make install"

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER="sap-dissector-wireshark"
