#!/usr/bin/env python
#####################################
# Installation module to install dradis as a service
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="BustedSec (Frank_Trezza)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will make the ptf dradis installation run as a service so it can be started\stopped with service dradis start or service dradis stop"
# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="git"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/BustedSec/dradis-service-installer"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION=""

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN=""

# DEPENDS FOR FEDORA INSTALLS
FEDORA=""

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},mv dradis.service /lib/systemd/system/"



