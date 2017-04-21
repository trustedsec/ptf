#!/usr/bin/env python
#####################################
# Installation module for nipe
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Ben Drysdale"

# DESCRIPTION OF THE MODULE
DESCRIPTION=“This module will install/update Nipe. Nipe is a perl script that routes all outbound traffic through the Tor network. Nipe was created by Heitor Gouvêa."

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/GouveaHeitor/nipe/"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="nipe"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,make,perl,perl-modules,libseccomp2,tor,torsocks"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,make,perl,perl-CPAN,libevent,tor,torsocks"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},export PERL_MM_USE_DEFAULT=1,cpan -f install Switch JSON LWP::UserAgent,nipe install"

# CREATE LAUNCHER
LAUNCHER="nipe"
