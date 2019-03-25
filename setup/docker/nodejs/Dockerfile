FROM docker.io/fedora:23
MAINTAINER Matthew Owens mowens@redhat.com
RUN dnf -y install dnf-plugins-core
RUN dnf copr enable -y mstuchli/Python3.5
RUN dnf -y install python35-python3 

RUN dnf groupinstall -y "Development Tools"

RUN dnf install -y \
   wget \
   tar \
   npm

#RUN dnf install -y \
#   wget \
#   tar \
#   nodejs

WORKDIR /home/container

ADD requirements.txt /home/container/
RUN pip3.5 install --upgrade pip
RUN pip3.5 install -r requirements.txt 
RUN npm install -g gulp bower 
RUN setcap cap_net_raw,cap_net_admin+p /usr/bin/ping
