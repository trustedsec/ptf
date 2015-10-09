#!/usr/bin/env python
#####################################
# Installation module for Burp
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="David Kennedy (ReL1K)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update the Burp Suite Free - web application attacks"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="FILE"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://portswigger.net/DownloadUpdate.ashx?Product=Free"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="burp"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="default-jre"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="java-1.8.0-openjdk"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},echo #!/bin/sh > burp.sh,echo java -jar burp.jar >> burp.sh,chmod +x burp.sh,mv DownloadUpdate.ashx?Product=Free burp.jar"

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER="burp"
