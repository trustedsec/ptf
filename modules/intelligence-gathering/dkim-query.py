#!/usr/bin/env python
#######################################
# Installation module for DKIM-Query
#######################################

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update DKIM-Query by TrailofBits - A tool to check a host's DKIM record"

AUTHOR="Andrew Schwartz"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/trailofbits/dkim-query.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="dkim-query"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,ruby,ruby-dev"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},gem install dkim-query"

LAUNCHER="dkim-query"

# PREREQ INSTALL MODULES NEEDED FOR THIS TOOL TO WORK PROPERLY
TOOL_DEPEND=""
