#!/usr/bin/env python
#######################################
# Installation module for RAWR
#######################################

# AUTHOR OF MODULE NAME
AUTHOR="Justin Herman (JDogHerman) & Jason Ashton (ninewires)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update RAWR - Rapid Assessment of Web Resources."

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/al14s/rawr.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="rawr"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,python-pip,libffi-dev,cmake qt4-qmake python-pil python-psutil python-qt4 python-netaddr python-pygraphviz python-pyside.qtwebkit xvfb"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},python -m pip install python_qt_binding xlsxwriter lxml rdpy, ./rawr.py -u -q"

# create a launcher
LAUNCHER="rawr"
