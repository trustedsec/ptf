#!/usr/bin/env python
#####################################
# Installation module for Ghostwriter
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Andrew Schwartz"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update Ghostwriter by Christopher Maddalena (@cmaddy) - The SpecterOps project management and reporting engine (https://ghostwriter.wiki/)"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/GhostManager/Ghostwriter"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="ghostwriter"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,docker"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,docker"

AFTER_COMMANDS="cd {INSTALL_LOCATION},mkdir .envs && cp -r .envs_template/.*.envs && docker-compose -f local.yml up -d,docker-compose -f local.yml run --rm django /seed_data,docker-compose -f local.yml run --rm django python manage.py createsuperuser"

# create a launcher
LAUNCHER="ghostwriter"

# PREREQ INSTALL MODULES NEEDED FOR THIS TOOL TO WORK PROPERLY
TOOL_DEPEND=""
