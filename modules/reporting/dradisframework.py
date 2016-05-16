#!/usr/bin/env python
#######################################
# Installation module for Dradis Framework
#######################################

# AUTHOR OF MODULE NAME
AUTHOR="Mauro Risonho de Paula Assumpcao (firebits)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update - Dradis is a collaboration and reporting platform"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/dradis/dradis-ce.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="dradisframework"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,ruby2.3,ruby-dev,ruby-rails,git,libmysqlclient-dev,libsqlite3-dev"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,ruby,rubygem-rails,git,libsqlite3x-devel"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},mkdir dradis-server,mv * dradis-server,cd dradis-server,cd bin,gem install bundler,gem install ruby-nmap,./setup,./bundle install,./setup"
