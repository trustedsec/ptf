#!/usr/bin/env python
#####################################
# Installation module for OneSixtyOne
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Steven van der Baan (vdbaan)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update onesixtyone (Portcullis Labs)."

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="FILE"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://labs.portcullis.co.uk/download/onesixtyone-0.7.tar.gz"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="onesixtyone"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,gcc,make"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,gcc,make"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},tar xzf onesixtyone-0.7.tar.gz, rm onesixtyone-0.7.tar.gz, cp onesixtyone-0.7/* {INSTALL_LOCATION},make,make install"
