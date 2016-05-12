#!/usr/bin/env python
#####################################
# Installation module for shellter
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="David Kennedy (HackingDave)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update Shellter Project - awesome AV evasion"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="FILE"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://www.shellterproject.com/Downloads/Shellter/Latest/shellter.zip"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="shellter"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="wine,curl"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="wine,curl"

# THIS WILL STILL RUN AFTER COMMANDS EVEN IF ITS ALREADY INSTALLED. USEFUL FOR FILE UPDATES AND WHEN NOT USING GIT OR OTHER APPLICATIONS THAT NEEDS AFTER COMMANDS EACH TIME
BYPASS_UPDATE="YES"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},unzip -j -o shellter.zip,rm shellter.zip,echo '#/bin/sh' > shellter.sh,echo 'wine shellter.exe' >> shellter.sh,chmod +x shellter.sh"

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER="shellter"

