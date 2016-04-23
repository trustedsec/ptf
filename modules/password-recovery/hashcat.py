#!/usr/bin/env python
#####################################
# Installation module for Hashcat
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Martin Bos (@purehate_)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update Hashcat - An advanced CPU-based password recovery"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/hashcat/hashcat.git"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="hashcat"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="libgmp3-dev:i386 libgmp3-dev git lzip gcc-multilib make m4 mingw-w64"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},wget -c https://gmplib.org/download/gmp/gmp-6.1.0.tar.lz,tar xf gmp-6.1.0.tar.lz,cp -af gmp-6.1.0 gmp-6.1.0-linux64,cd {INSTALL_LOCATION}gmp-6.1.0-linux64,./configure --host=x86_64-pc-linux-gnu --prefix={INSTALL_LOCATION}deps/gmp/linux64 --disable-shared,make install,cd {INSTALL_LOCATION},rm -rf gmp-6.1.0-linux64,make linux"


# DONT RUN AFTER COMMANDS ON UPDATE
BYPASS_UPDATE=NO

# LAUNCHER
LAUNCHER="hashcat"

