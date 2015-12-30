#!/usr/bin/env python
#####################################
# Installation module for wpscan
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Mauro Risonho de Paula Assumpcao (firebits)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update wpscan - a black box WP scanner"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/wpscanteam/wpscan/"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="wpscan"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git ruby ruby-dev libcurl4-openssl-dev make"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,ruby,ruby-devel,libcurl-devel,make"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},gem install bundler,bundle install,ruby wpscan.rb --update,echo '#!/bin/sh' > wpscan,echo 'ruby {INSTALL_LOCATION}wpscan.rb $@' >> wpscan,chmod +x wpscan"
# ALWAYS RUN UPDATES
BYPASS_UPDATE="YES"

# LAUNCHER SHORTCUT
LAUNCHER="wpscan"
