#!/bin/bash

# Install via the following commands:
# chmod +x install.sh
# sudo ./install.sh
# sudo reboot

# Make sure only root can run our script
if [[ $EUID -ne 0 ]]; then
   echo "Plesae runn as root via sudo ./install.sh" 1>&2
   exit 1
fi

############
### Check for network connection
###########
echo -e "\nChecking for Internet connection..."
ping -c 3 github.com &> /dev/null
if [ $? -ne 0 ]; then
    echo "------------------------------------"
    echo "Could not ping github.com. Are you sure you have a working Internet connection?"
    echo "Installer will exit, because it needs to fetch code from github.com"
    exit 1    
fi
echo -e "Success!\n"


while true; do
    read -p "Would you like run apt-get update & apt-get upgrade? (y/n): " yn
    case $yn in
        [Yy]* ) apt-get -y update; apt-get -y upgrade; break;;
        [Nn]* ) break;;
        * ) echo "(Y/N)";;
    esac
done

echo -e "\n*** Installing/updating required packages... ***\n"
#Install pip (package installer):
apt-get -y install python-setuptools
easy_install pip
apt-get -y install python-dev
apt-get -y install libpcre3-dev
pip install -r requirements.txt

echo  "\n*** Initializing config file ***\n"
python main.py --default-configs

while true; do
    read -p "Run automatically? (y/n): " yn
    case $yn in
        [Yy]* ) sed "s@#DIR#@${PWD}@g" config/planter-mcplantface-boot > /etc/init.d/planter-mcplantface-boot

    chmod 755 /etc/init.d/planter-mcplantface-boot;
		update-rc.d planter-mcplantface-boot defaults;
		break;;
        [Nn]* ) break;;
        * ) echo "Please select (y/n): ";;
    esac
done


while true; do
    read -p "Reboot? (y/n): " yn
    case $yn in
        [Yy]* ) reboot; break;;
        [Nn]* ) break;;
        * ) echo "Please select (y/n): ";;
    esac
done