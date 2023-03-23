#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
export PATH="$DIR:$PATH"
mv encryt_file.py encryption-tool
chmod +x encryption-tool