#!/usr/bin/env python
#####################################
# Installation module for prowl
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Nick Dyer"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update Prowl - LinkedInCrawler"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/Pickfordmatt/Prowl.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="prowl"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="python python-pip"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="pip install argparse BeautifulSoup urllib3 gitpython colorama, cd {INSTALL_LOCATION} && chmod +x prowl.py"

# CREATE LAUNCHER
LAUNCHER="prowl"
