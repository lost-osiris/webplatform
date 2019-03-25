#FROM mongo:latest
FROM cee-tools-base-mongodb:latest
MAINTAINER Matthew Owens mowens@redhat.com

RUN dnf install -y numactl

VOLUME "/data/db/"
VOLUME "/home/container/config/"
VOLUME "/home/container/actions/"
VOLUME "/home/cee-tools/logs/"

EXPOSE 27217

RUN chown -R mongodb:mongodb /data

RUN mkdir -p /home/cee-tools/mongodb

RUN mkdir -p /data/db /data/configdb 
RUN chown -R mongodb:mongodb /data/db /data/configdb

ADD entry.sh /home/container/
CMD /home/container/entry.sh
