#!/usr/bin/env python
#######################################
# Installation module for Dradis Framework
#######################################

# AUTHOR OF MODULE NAME
AUTHOR="Mauro Risonho de Paula Assumpcao (firebits)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update The Dradis Framework is an open-source collaboration and reporting platform for IT security experts."

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/dradis/dradisframework.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="dradisframework"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="ruby1.9.1,ruby-rails-3.2,ruby-all-dev,git"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},git checkout dradis3_blackhat-arsenal,ruby bin/setup,bundle exec rails server,exit"
