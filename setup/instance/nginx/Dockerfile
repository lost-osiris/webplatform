FROM cee-tools-base-nginx:latest
MAINTAINER Matthew Owens mowens@redhat.com

VOLUME "/home/container/config/"
VOLUME "/home/container/actions/"
VOLUME "/home/cee-tools/setup/"
VOLUME "/home/cee-tools/logs/"

VOLUME "/home/cee-tools/frontend/"

EXPOSE 8000

#RUN dnf install -y sudo

#RUN useradd -ms /bin/bash mowens && echo "docker:docker" | chpasswd && adduser docker sudo

#USER mowens
ADD entry.sh /home/container/
ENTRYPOINT /home/container/entry.sh
