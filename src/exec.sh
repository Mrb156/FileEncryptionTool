#!/bin/bash

# Set global environment variable for the script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
echo export PATH=$DIR:\$PATH >> $HOME/.bashrc
mv encrypt_file.py encryption-tool
chmod +x encryption-tool

# Check if pip is installed, and install it if necessary
if ! command -v pip &> /dev/null; then
    echo "Installing pip..."
    sudo apt-get update
    sudo apt-get install -y python3-pip
fi

# Install packages from requirements.txt
echo "Installing required packages..."
pip install -r requirements.txt