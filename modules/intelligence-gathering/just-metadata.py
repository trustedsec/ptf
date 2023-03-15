#####################################
# Installation module for Just-Metadata
#####################################

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update Just-Metadata by Chris Truncer - A tool that gathers and analyzes metadata about IP addresses. It attempts to find relationships between systems within a large dataset."

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

AUTHOR="Andrew Schwartz"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/FortyNorthSecurity/Just-Metadata"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="just-metadata"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION}/setup,./setup.sh"

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER="just-metadata"

# PREREQ INSTALL MODULES NEEDED FOR THIS TOOL TO WORK PROPERLY
TOOL_DEPEND=""
