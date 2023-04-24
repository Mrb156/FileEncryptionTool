#!/bin/bash
echo Install python
sudo apt-get install python3

# Set color for commands
RED="\033[31m"
NORMAL="\033[0;39m"

# Set global environment variable for the script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
echo export PATH=$DIR:\$PATH >> $HOME/.bashrc
mv encrypt_file.py encryption-tool
chmod +x encryption-tool

mv zipper.py compress-tool
chmod +x compress-tool

# Check if pip is installed, and install it if necessary
if ! command -v pip &> /dev/null; then
    echo -e $RED "Installing pip..." $NORMAL
    sudo apt-get update
    sudo apt-get install -y python3-pip
fi

# Install packages from requirements.txt
echo -e $RED "Installing required packages..." $NORMAL
pip install -r requirements.txt