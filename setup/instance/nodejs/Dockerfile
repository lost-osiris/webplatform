FROM cee-tools-base-nodejs:latest 
MAINTAINER Matthew Owens mowens@redhat.com

VOLUME "/home/cee-tools/controller/" 
VOLUME "/home/cee-tools/source/"
VOLUME "/home/cee-tools/settings/"
VOLUME "/home/container/daemon/"
VOLUME "/home/cee-tools/logs/"

EXPOSE 3000 

CMD /home/container/daemon/daemon.sh devel
