#!/bin/bash

# Set color for commands
RED="\033[31m"
NORMAL="\033[0;39m"

# Install python
echo Installing python
sudo apt-get install python3


# Set global environment variable for the script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
echo export PATH=$DIR:\$PATH >> $HOME/.bashrc

# Rename the python files for easier access
mv encrypt_file.py encrypt
chmod +x encrypt

mv zipper.py compress
chmod +x compress

# Check if pip is installed, and install it if necessary
if ! command -v pip &> /dev/null; then
    echo -e $RED "Installing pip..." $NORMAL
    sudo apt-get update
    sudo apt-get install -y python3-pip
fi

# Install packages from requirements.txt
echo -e $RED "Installing required packages..." $NORMAL
pip install -r requirements.txt
sudo apt-get install linux_requirements.txt