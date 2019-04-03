FROM debian:sid
LABEL version="1.1"
LABEL description="Dockerized version of Trustedsec PTF - Penetration Testing Framework"
LABEL author="Jacobo Avariento Gimeno"
COPY .bashrc /root/.bashrc
COPY bootstrap.sh /root/bootstrap.sh
RUN bash -c /root/bootstrap.sh
