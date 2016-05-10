#!/usr/bin/env python
#####################################
# Installation module for fierce
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Jason Ashton (@jayw0k)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update fierce - domain scanner"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/davidpepper/fierce-domain-scanner.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="fierce"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,perl"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,perl,perl-CPAN"

# COMMANDS TO RUN AFTER 
AFTER_COMMANDS="export PERL_MM_USE_DEFAULT=1,export PERL_EXTUTILS_AUTOINSTALL='--defaultdeps',cpan -i strict Net::hostent Net::DNS IO::Socket Socket Getopt::Long"

# create a launcher
LAUNCHER="fierce"
