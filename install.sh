# getting ready to install docker and be able to setup controller
dnf -y install python-virtualenv dnf-plugins-core
dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo

# setting up mongodb
MONGO_REPO="[mongodb-org-3.4]
\nname=MongoDB Repository
\nbaseurl=https://repo.mongodb.org/yum/redhat/7/mongodb-org/3.4/x86_64/
\ngpgcheck=1
\nenabled=1
\ngpgkey=https://www.mongodb.org/static/pgp/server-3.4.asc"
echo $MONGO_REPO > /etc/yum.repos.d/mongodb-org-3.4.repo

# installing mongodb and docker
dnf -y install mongodb-org docker-ce nodejs npm

# setup frontend
cd ./frontend
npm install -g n
n latest
npm install
