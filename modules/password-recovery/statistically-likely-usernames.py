#!/usr/bin/env python
#######################################
# Installation module for statistically likely username lists
#######################################
AUTHOR="Justin Bollinger (Bandrel)"

DESCRIPTION="This module will install/update the statistically likely username project from insidetrust"

INSTALL_TYPE="GIT"

REPOSITORY_LOCATION="https://github.com/insidetrust/statistically-likely-usernames.git"

INSTALL_LOCATION="statistically-likely-usernames"

DEBIAN="git"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION}, cd ..,if [ -d '/usr/share/wordlists/' ]; then ln -s `pwd`/statistically-likely-usernames /usr/share/wordlists/; fi;"
