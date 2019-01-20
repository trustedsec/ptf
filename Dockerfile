LABEL version="1.0"
LABEL description="Dockerized version of Trustsec PTF - Penetration Testing Framework"
LABEL author="Jacobo Avariento Gimeno"
FROM debian:sid
COPY bootstrap.sh /bootstrap.sh
RUN /bootstrap.sh
