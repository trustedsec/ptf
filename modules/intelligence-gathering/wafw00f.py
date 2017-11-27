#!/usr/bin/env python
#####################################
# Installation module for wafw00f
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Gareth Darby (gazcbm) based on the original module by Steven van der Baan (vdbaan) "

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update wafw00f (Sandro Gauci && Wendel G. Henrique)."

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/sandrogauci/wafw00f.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="wafw00f"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git, python-pip"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git, python-pip"

# DEPENDS FOR ARCHLINUX INSTALLS
ARCHLINUX=""

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},python setup.py install, mv {INSTALL_LOCATION}/wafw00f/main.py {INSTALL_LOCATION}/wafw00f.py"

# CREATE LAUNCHER
LAUNCHER="wafw00f"
