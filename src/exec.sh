#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
echo export PATH=$DIR:\$PATH >> $HOME/.bashrc
mv encrypt_file.py encryption-tool
chmod +x encryption-tool