#!/usr/bin/env python
#####################################
# Installation module for DNSEnum
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Dave Kennedy (HackingDave)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update dnsenum - a DNS scanning tool"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/fwaeytens/dnsenum"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="dnsenum"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git,perl"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,perl,perl-CPAN"

# COMMANDS TO RUN AFTER 
AFTER_COMMANDS="export PERL_MM_USE_DEFAULT=1,export PERL_EXTUTILS_AUTOINSTALL='--defaultdeps',yes | cpan -fi Net::IP Net::DNS Net::Netmask Net::Whois::IP HTML::Parser WWW::Mechanize XML::Writer String::Random"

# create a launcher
LAUNCHER="dnsenum"
