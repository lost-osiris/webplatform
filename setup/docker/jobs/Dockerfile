FROM docker.io/fedora:24
MAINTAINER Matthew Owens mowens@redhat.com

RUN dnf groupinstall -y "Development Tools"

RUN dnf install -y \
   wget \
   tar \
   gcc \
   redhat-rpm-config \
   mysql mysql-devel \
   python3-devel \
   iputils \
   python-pip \
   procps

WORKDIR /home/container

ADD requirements.txt /home/container/

RUN pip3.5 install --upgrade pip
RUN pip3.5 install -r requirements.txt
RUN setcap cap_net_raw,cap_net_admin+p /usr/bin/ping
