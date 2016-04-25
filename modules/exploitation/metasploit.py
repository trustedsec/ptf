#!/usr/bin/env python
#####################################
# Installation module for Metasploit
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="David Kennedy (ReL1K)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update Metasploit"

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/rapid7/metasploit-framework"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="metasploit"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="ruby ruby2.3 ruby2.3-dev nmap git-core curl zlib1g-dev build-essential libpq5 libpq-dev libssl-dev libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev libcurl4-openssl-dev software-properties-common libffi-dev libpcap-dev autoconf postgresql libgmp-dev"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git,make,automake,gcc,gcc-c++,kernel-devel,postgresql-server,postgresql-devel,libpcap-devel,sqlite-devel,ruby-irb,rubygems,rubygem-nokogiri,rubygem-ffi,rubygem-bigdecimal,rubygem-rake,rubygem-i18n,rubygem-bundler,ruby-devel,sqlite,rubygem-sqlite3,git,libxml2-devel,patch"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS="cd {INSTALL_LOCATION},gem outdated,gem update,gem install rails,gem install bundler,bundle install,cd /usr/local/bin,gem outdated,gem update,gem install rails,gem install bundler,bundle install,cd {INSTALL_LOCATION},gem install bundler,bundler install,bundle install,ln -s /pentest/exploitation/metasploit/msfconsole /usr/local/bin/msfconsole"

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER="msfbinscan,msfd,msfelfscan,msfmachscan,msfpescan,msfrop,msfrpc,msfrpcd,msfupdate,msfvenom"
