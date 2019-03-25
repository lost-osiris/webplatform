FROM docker.io/fedora:24
MAINTAINER Matthew Owens mowens@redhat.com

RUN groupadd -r mongodb && useradd -r -d /home/mongodb/ -g  mongodb mongodb

#RUN dnf -y install dnf-plugins-core
#RUN dnf copr enable -y mstuchli/Python3.5
#RUN dnf -y install python35-python3
RUN dnf -y install iputils  python-pip git openssl openssl-devel procps

ADD mongodb-org-3.2.repo /etc/yum.repos.d/
RUN dnf -y install mongodb-org

WORKDIR /home/container

# ADD requirements.txt /home/container/

# RUN pip3 install --upgrade pip
# RUN pip3 install -r requirements.txt
RUN setcap cap_net_raw,cap_net_admin+p /usr/bin/ping
RUN mkdir /home/container/daemon/
RUN usermod mongodb -a -G wheel
