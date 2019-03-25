FROM cee-tools-base-jobs:latest
MAINTAINER Matthew Owens mowens@redhat.com


VOLUME "/home/container/config/"
VOLUME "/home/container/actions/"
VOLUME "/home/cee-tools/setup/instances/"
VOLUME "/home/cee-tools/logs/"
VOLUME "/home/cee-tools/api/"
VOLUME "/home/cee-tools/scripts/"

ADD entry.sh /home/container/
ENTRYPOINT /home/container/entry.sh
