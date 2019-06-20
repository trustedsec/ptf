#!/bin/bash
#
# Commands run by Docker when building the docker container with PTF framework
#
# Author: Jacobo Avariento Gimeno
#

echo "docker-ptf" > /etc/hostname
apt-get update
apt-get upgrade -y
apt-get install -y python git sudo locate vim pip tcpdump net-tools #libgmp3-dev:i386
cd /tmp
wget http://http.kali.org/pool/main/u/unicornscan/unicornscan_0.4.7-1kali2_amd64.deb
dpkg -i ./unicornscan_0.4.7-1kali2_amd64.deb
cd /root
git clone https://github.com/trustedsec/ptf.git
cd ptf
echo -en "use modules/install_update_all\nyes\n" | python ptf
echo
echo
echo "** DONE **"
echo "PTF is built and ready to use."
exit 0
