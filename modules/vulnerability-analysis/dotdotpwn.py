#!/usr/bin/env python
#####################################
# Installation module for DotDotPwn
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Mauro Risonho de Paula Assumpcao (firebits)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update DotDotPwn - The Directory Traversal Fuzzer"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/wireghoul/dotdotpwn.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="dotdotpwn"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="perl,nmap,libnet-inet6glue-perl,libnet-scp-perl,libnet-server-perl,tftp,libdbix-profile-perl,libmoosex-role-timer-perl,socket,libio-socket-ssl-perl"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,perl,nmap,perl-Net-SFTP,perl-Net-FTP-RetrHandle,tftp,perl-Time-HiRes,perl-IO-Socket-IP,perl-MooseX-Getopt,perl-Switch,perl-Net-SSLeay"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},export PERL_MM_USE_DEFAULT=1,export PERL_EXTUTILS_AUTOINSTALL='--defaultdeps',cpan -fi Switch TFTP "
