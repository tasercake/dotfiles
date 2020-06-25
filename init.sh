#!/bin/sh
# Install Miniconda
MINICONDA_INSTALL_DIR="${HOME}/miniconda"
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda3.sh
bash miniconda3.sh -p $MINICONDA_INSTALL_DIR
