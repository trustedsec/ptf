#!/usr/bin/env python
#####################################
# Installation module for Nessus Parser
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Larry Spohn (Spoonman)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update Nessus Parser - a Nessus results parsing tool"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="FILE"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="http://www.melcara.com/wp-content/uploads/2017/09/parse_nessus_xml.v24.pl_.zip"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="nessus_parser"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="perl"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="perl,perl-CPAN"

# DON'T RUN AFTER COMMANDS ON UPDATE
BYPASS_UPDATE="NO"

# COMMANDS TO RUN AFTER 
AFTER_COMMANDS="cd {INSTALL_LOCATION},unzip -j -o parse_nessus_xml.v24.pl_.zip,rm parse_nessus_xml.v24.pl_.zip,sed -i.bak 's_#!/opt/local/bin/perl_#!/usr/bin/env perl_g' parse_nessus_xml.v24.pl,mv parse_nessus_xml.v24.pl nessus_parser.pl,chmod +x nessus_parser.pl,export PERL_MM_USE_DEFAULT=1,export PERL_EXTUTILS_AUTOINSTALL='--defaultdeps',yes | cpan -fi XML::TreePP XML::TreePP Math::Round Excel::Writer::XLSX Data::Table Excel::Writer::XLSX::Chart Getopt::Std"

# create a launcher
LAUNCHER="nessus_parser"
