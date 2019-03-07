#!/bin/bash
#
# Commands run by Docker when building the docker container with PTF framework
#
#
echo "docker-ptf" > /etc/hostname
apt-get update
apt-get upgrade -y
apt-get install -y python git sudo locate vim #libgmp3-dev:i386
cd /root
git clone https://github.com/spinfoo/ptf.git
cd ptf
git checkout docker
git pull origin docker
echo -en "use modules/install_update_all\nyes\n" | python ptf
echo
echo
echo "** DONE **"
echo "PTF is built and ready to use."
exit 0
