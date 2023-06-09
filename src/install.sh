#!/bin/bash

# Set color for commands
ALERT="\033[0;35m"
NORMAL="\033[0;39m"

system_update(){
    sudo apt-get -y update
    sudo apt-get -y upgrade
}

add_deps(){
    # Install python
    echo -e $ALERT Installing python $NORMAL
    sudo apt-get install python3


    # Set global environment variable for the script
    DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
    echo export PATH=$DIR:\$PATH >> $HOME/.bashrc
    echo source ~/.bashrc


    # Rename the python files for easier access
    mv encrypt_file.py encrypt
    chmod +x encrypt

    mv zipper.py compress
    chmod +x compress

    # Check if pip is installed, and install it if necessary
    if ! command -v pip &> /dev/null; then
        echo -e $ALERT "Installing pip..." $NORMAL
        sudo apt-get update
        sudo apt-get install -y python3-pip
    fi

    # Install packages from requirements.txt
    echo -e $ALERT "Installing required packages..." $NORMAL
    pip install -r requirements.txt
}

# Update system before installing
read -p "I recommend to update your system before installing dependencies. Do you want to update the OS? (y/n) " yn
case $yn in
    [yY] ) echo -e $ALERT Ok, I update the system. $NORMAL;
        system_update
        add_deps
        
        break;;
    [nN] ) echo -e $ALERT Ok, installing only dependencies. $NORMAL;
       add_deps

        break;;
    * ) echo -e $ALERT invalid response;;
esac
done
