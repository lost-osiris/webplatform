#!/bin/bash -x
INSTANCE=$1

if [ ! -d "/home/container/source/nodejs/node_modules" ] ; then
   cd /home/cee-tools/source/nodejs/
   npm install
fi

/home/cee-tools/controller/container/ctl $INSTANCE start nodejs 

while true; do
   sleep 600
done
