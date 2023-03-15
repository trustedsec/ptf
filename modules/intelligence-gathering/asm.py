#!/usr/bin/env python
#######################################
# Installation module for AttackSurfaceMapper
#######################################

DESCRIPTION="This module will install/update Attack Surface Mapper (ASM) by Andreas Georgiou - A tool that aim to automate the recon process"

AUTHOR="Andrew Schwartz"

INSTALL_TYPE="GIT"

REPOSITORY_LOCATION="https://github.com/superhedgy/AttackSurfaceMapper.git"

INSTALL_LOCATION="ASM"

DEBIAN="python3,pip"

AFTER_COMMANDS="cd {INSTALL_LOCATION},python3 -m pip install --no-cache-dir -r requirements.txt"
