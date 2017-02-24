#!/usr/bin/env python
##########################################
# Installation module for tweets_analyzer
##########################################

# AUTHOR OF MODULE NAME
AUTHOR="Ben Drysdale"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update tweets_analyzer by x0rz - Tweets metadata scraper & activity analyzer."

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/x0rz/tweets_analyzer/"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="tweets_analyzer"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,python,python-dev,python-pip"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,python,python-devel,python-pip"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},pip install -r requirements.txt"

# CREATE LAUNCHER
LAUNCHER="tweets_analyzer"
