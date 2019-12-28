#!/usr/bin/env python
#######################################
# Installation module for NTLMRecon
#######################################

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update NTLMRecon by Sachin S. Kamath - A fast NTLM reconnaissance tool without external dependencies. Useful to find out information about NTLM endpoints when working with a large set of potential IP addresses and domains."

AUTHOR="Andrew Schwartz"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/sachinkamath/ntlmrecon.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="ntlmrecon"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,pip,python"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},pip install virtualenv,virtualenv venv,source venv/bin/activate,python setup.py install"

LAUNCHER="ntlmrecon"

# PREREQ INSTALL MODULES NEEDED FOR THIS TOOL TO WORK PROPERLY
TOOL_DEPEND=""
